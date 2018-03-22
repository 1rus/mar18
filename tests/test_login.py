from hrmsm.pages.login_page import LoginPage
from hrmsm.base.FrameTest import FrameTestCase
import pytest


title = 'OrangeHRM'
success = 'Welcome Admin'
empty_pass = 'Password cannot be empty'
invalid_creds = 'Invalid credentials'


@pytest.mark.incremental
class Test_Login(FrameTestCase):


    def test_valid_login(self):
        page = LoginPage(self.driver)
        page.open()
        page.login_with(username='admin', password='Password')
        self.assertions.verify_equal(page.title(), title)
        self.assertions.verify_equal(self.driver.find_element_by_id('welcome').text, success)

    def test_logout(self):
        page = LoginPage(self.driver)
        page.open()
        page.login_with(username='admin', password='Password')
        self.assertions.verify_true(self.driver.current_url.endswith('login'))

    def test_empty_password(self):
        page = LoginPage(self.driver)
        page.open()
        page.login_with(username='admin', password='')
        mes = page.get_error_message()
        print(mes)
        self.assertions.verify_equal(page.title(), title)
        self.assertions.verify_equal(mes, empty_pass, None)

    def test_invalid_login(self):
        page = LoginPage(self.driver)
        page.open()
        page.login_with(username='Admin', password='password')
        mes = page.get_error_message()
        print(mes)
        self.assertions.verify_equal(page.title(), title)
        self.assertions.verify_equal(mes, invalid_creds, None)
