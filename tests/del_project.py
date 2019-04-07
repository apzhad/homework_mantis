import random
from model.project import Project


def test_del_project(gen):
    old_list = gen.project.get_project_list()
    del_project = random.choice(old_list)
    gen.project.delete_project(del_project)
    new_list = gen.project.get_project_list()
    assert len(old_list)-1 == len(new_list)
    old_list.remove(del_project)
    assert sorted(old_list, key=Project.sort_by_name) == sorted(new_list, key=Project.sort_by_name)
