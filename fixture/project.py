from selenium.webdriver.support.ui import Select
from model.project import Project
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import re


class ProjectManage:

    def __init__(self, gen):
        self.gen = gen

    def open_create_project(self):
        wd = self.gen.wd
        if not (wd.current_url.endswith("/manage_proj_create_page.php") and len(
                wd.find_elements_by_xpath("//input[@value='Add Project']")) > 0):
            if not (wd.current_url.endswith("/manage_proj_page.php") and len(
                    wd.find_elements_by_link_text("Name")) > 0):
                self.open_manage_project()
                wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_xpath("//input[@value='Add Project']")

    def open_manage_project(self):
        wd = self.gen.wd
        if not (wd.current_url.endswith("/manage_overview_page.php") or wd.current_url.endswith("/manage_proj_page.php")):
            wd.find_element_by_link_text("Manage").click()
        elif wd.current_url.endswith("/manage_overview_page.php") and len(
                wd.find_elements_by_link_text("Manage Projects")) > 0:
            wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_xpath("//input[@value='Create New Project']")

    def set_field_value(self, field_name, text):
        wd = self.gen.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
        wd.find_element_by_name(field_name).send_keys(text)

    def select_from_list(self, list_name, text):
        wd = self.gen.wd
        if text is not None:
            wd.find_element_by_name(list_name).click()
            Select(wd.find_element_by_name(list_name)).select_by_visible_text(text)

    def create_project(self, project):
        wd = self.gen.wd
        self.open_create_project()
        # заполняем имя проекта
        self.set_field_value("name", project.name)
        # выбираем статус проекта
        self.select_from_list("status", project.status)
        if project.change_inherit_global:
            wd.find_element_by_name("inherit_global").click()
        self.select_from_list("view_state", project.view_status)
        # описание проекта
        self.set_field_value("description", project.description)
        # добавляем проект
        wd.find_element_by_xpath("//input[@value='Add Project']")
        self.return_to_project_page()

    def return_to_project_page(self):
        wd = self.gen.wd
        wd.find_element_by_link_text("Proceed").click()
        wd.find_element_by_xpath("//input[@value='Add Project']")


