import random
import string


def random_username(prefix, max_length):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_length))])


def test_signup_new_account(gen):
    username = random_username("user_", 10)
    password = "pass"
    email = username + "@localhost"
    gen.james.ensure_user_exists(username, password)
    gen.signup.new_user(username, password, email)
    assert gen.soap.can_login(username, password)
    gen.session.login(username, password)
    assert gen.session.is_login_as(username)
    gen.session.logout()

