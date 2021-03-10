from Pages.HomePage import HomePage
from TestCase.test_base import BaseTest
import pytest


class TestNavigationMenu(BaseTest):

    #@pytest.mark.skip(reason="no way of currently testing this")
    def test_timeline_page(self):
        global page
        page = HomePage(self.driver)
        page = page.timeline_menu_click()
        assert page.get_title() == 'Timeline'

    def test_register_page(self):
        global page
        page = page.register_menu_click()
        assert page.get_title() == 'Register'

    def test_login_page(self):
        global page
        page = page.login_menu_click()
        assert page.get_title() == 'Login'

    def test_home_page(self):
        global page
        page = page.home_menu_click()
        assert page.get_title() == 'Random Quotes'
