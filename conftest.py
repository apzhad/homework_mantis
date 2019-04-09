import pytest
from fixture.generic import Generic
import json
import os.path
import ftputil

fixture = None
settings = None


def load_config(file):
    global settings
    if settings is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            settings = json.load(f)
    return settings


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--settings"))


@pytest.fixture
def gen(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    # login_info = config["webadmin"]
    if fixture is None or not fixture.is_valid():
        fixture = Generic(browser=browser, config=config)
    # fixture.session.ensure_login(username=login_info["username"], password=login_info["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def configure_server(request, config):
    install_server_conf(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])

    def fin():
        restore_server_conf(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])
    request.addfinalizer(fin)


def install_server_conf(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile("config_inc.php.bak"):
            remote.remove("config_inc.php.bak")
        if remote.path.isfile("config_inc.php"):
                remote.rename("config_inc.php", "config_inc.php.bak")
        remote.upload((os.path.join(os.path.dirname(__file__), "resources/config_inc.php")), "config_inc.php")


def restore_server_conf(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile("config_inc.php.bak"):
            if remote.path.isfile("config_inc.php"):
                remote.remove("config_inc.php")
            remote.rename("config_inc.php.bak", "config_inc.php")


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
