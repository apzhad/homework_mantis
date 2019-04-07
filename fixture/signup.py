import re


class SignupManage:

    def __init__(self, gen):
        self.gen = gen

    def new_user(self, username, password, email):
        wd = self.gen.wd
        wd.get(self.gen.base_url + "/signup_page.php")
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_css_selector("input[type='submit']").click()

        mail = self.gen.mail.get_mail("[MantisBT] Account registration")
        url = self.extract_confirm_url(mail)

        wd.get(url)
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("password1").send_keys(password)
        wd.find_element_by_css_selector("input[type='submit']").click()

    def extract_confirm_url(self, text):
        return re.search("http://.*$", text).group(0)