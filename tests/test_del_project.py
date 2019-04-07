import random
from model.project import Project


def test_del_project(gen):
    username = gen.config["webadmin"]["username"]
    password = gen.config["webadmin"]["password"]
    gen.session.ensure_login(username=username, password=password)
    if gen.soap.get_project_list(username, password) == 0:
        gen.project.create_project(Project(name="name", status="release", inherit_global=False, view_status="public"))
    old_list = gen.soap.get_project_list(username, password)
    del_project = random.choice(old_list)
    gen.project.delete_project(del_project)
    new_list = gen.soap.get_project_list(username, password)
    assert len(old_list)-1 == len(new_list)
    old_list.remove(del_project)
    assert sorted(old_list, key=Project.sort_by_name) == sorted(new_list, key=Project.sort_by_name)
