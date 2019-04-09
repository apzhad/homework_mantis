from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapManage:
    def __init__(self, gen):
        self.gen = gen

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username=None, password=None):
        if username is None:
            username = self.gen.config["webadmin"]["username"]
        if password is None:
            password = self.gen.config["webadmin"]["password"]
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        project_data = client.service.mc_projects_get_user_accessible(username, password)
        project_list = []
        for data in project_data:
            project_list.append(Project(name=data.name, status=data.status.name, view_status=data.view_state.name,
                                        description=data.description))
        return project_list
