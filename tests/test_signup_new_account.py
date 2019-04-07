def test_signup_new_account(gen):
    username = "user1"
    password = "pass"
    gen.james.ensure_user_exists(username, password)
