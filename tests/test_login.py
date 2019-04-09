def test_login(gen):
    if gen.session.is_login():
        gen.session.logout()
    gen.session.login("administrator", "root")
    assert gen.session.is_login_as("administrator")
    gen.session.logout()
