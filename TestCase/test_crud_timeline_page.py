from Pages.HomePage import HomePage
from TestCase.test_base import BaseTest
import pytest


class TestCrudTimelinePage(BaseTest):

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_timeline_page(self):
        global page
        page = HomePage(self.driver)
        page = page.timeline_menu_click()
        name = page.list_user()
        import logging
        logging.getLogger().info(name)
