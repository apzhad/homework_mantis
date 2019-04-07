from model.project import Project
import random
import string
import pytest


def random_string(prefix, max_length):
    symbols = string.ascii_letters + string.digits + ' '*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_length))])


status = ["stable", "development", "release", "obsolete"]
view_status = ["public", "private"]


test_data = [Project(name=random_string("name", 10), status=random.choice(status),
                     view_status=random.choice(view_status), description=random_string("descr", 30))
             for i in range(5)]


@pytest.mark.parametrize("project", test_data, ids=[repr(x) for x in test_data])
def test_add_project(gen, project):
    old_list = gen.project.get_project_list()
    gen.project.create_project(project)
    new_list = gen.project.get_project_list()
    assert len(old_list)+1 == len(new_list)
    old_list.append(project)
    assert sorted(old_list, key=Project.sort_by_name) == sorted(new_list, key=Project.sort_by_name)

