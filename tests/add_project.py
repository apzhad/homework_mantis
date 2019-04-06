from model.project import Project


def test_add_project(gen):
    pr = Project(name="test", status="stable", change_inherit_global=False, view_status="public", description="sbdfvj")
    gen.project.create_project(pr)
