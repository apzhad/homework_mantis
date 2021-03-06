class Project:

    def __init__(self, name=None, status=None, inherit_global=False, view_status=None, description=None,
                 id=None):
        self.name = name
        self.status = status
        self.inherit_global = inherit_global
        self.view_status = view_status
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.id, self.name, self.status, self.view_status, self.description)

    def __eq__(self, other):
        return self.name == other.name and (
                self.id is None or other.id is None or self.id == other.id) and self.status == other.status

    def sort_by_name(self):
        return self.name
