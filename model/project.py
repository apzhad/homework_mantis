class Project:

    def __init__(self, name=None, status=None, inherit_global=None, view_status=None, description=None):
        self.name = name
        self.status = status
        self.inherit_global = inherit_global
        self.view_status = view_status
        self.description = description
