from suds.client import Client
from suds import WebFault


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
