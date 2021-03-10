from Pages.HomePage import HomePage
from TestCase.test_base import BaseTest
import pytest


class TestAccount(BaseTest):
    USERNAME = 'foobar'
    EMAIL = 'foo@bar.baz'
    PASSWORD = 1234

    #@pytest.mark.skip(reason="no way of currently testing this")
    def test_register(self):
        global page
        page = HomePage(self.driver)
        page = page.register_menu_click()
        page.register_account(
                self.USERNAME, self.EMAIL,
                self.PASSWORD, self.PASSWORD)
        assert page.account_menu().text() == self.USERNAME
        page = page.logout_menu_click()

    def test_login(self):
        global page
        page = page.login_menu_click()
        page.login_account(self.EMAIL, self.PASSWORD)
        assert page.account_menu().text() == self.USERNAME
