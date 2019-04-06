import pytest
from fixture.generic import Generic
import json
import os.path

fixture = None
settings = None


def load_config(file):
    global settings
    if settings is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            settings = json.load(f)
    return settings


@pytest.fixture
def gen(request):
    global fixture
    browser = request.config.getoption("--browser")
    url = load_config(request.config.getoption("--settings"))["web"]
    login_info = load_config(request.config.getoption("--settings"))["webadmin"]
    if fixture is None or not fixture.is_valid():
        fixture = Generic(browser=browser, base_url=url["base_url"])
    fixture.session.ensure_login(username=login_info["username"], password=login_info["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.finish()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--settings", action="store", default="settings.json")
