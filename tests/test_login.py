def test_login(gen):
    gen.session.login("administrator", "root")
    assert gen.session.is_login_as("administrator")
