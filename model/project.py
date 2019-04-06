class Project:

    def __init__(self, name=None, status=None, change_inherit_global=False, view_status=None, description=None,
                 id=None):
        self.name = name
        self.status = status
        self.change_inherit_global = change_inherit_global
        self.view_status = view_status
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.id, self.name, self.status, self.view_status, self.description)

