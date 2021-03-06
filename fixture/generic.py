# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionManage
from fixture.project import ProjectManage
from fixture.james import JamesManage
from fixture.mail import MailManage
from fixture.signup import SignupManage
from fixture.soap import SoapManage


class Generic:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "edge":
            self.wd = webdriver.Edge()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.base_url = config["web"]["base_url"]
        self.config = config
        self.wd.implicitly_wait(1)
        self.session = SessionManage(self)
        self.project = ProjectManage(self)
        self.james = JamesManage(self)
        self.mail = MailManage(self)
        self.signup = SignupManage(self)
        self.soap = SoapManage(self)

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def finish(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
