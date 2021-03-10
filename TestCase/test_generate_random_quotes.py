from Pages.HomePage import HomePage
from TestCase.test_base import BaseTest
import pytest
import logging


class TestGenerateRandomQuotes(BaseTest):

    #@pytest.mark.skip(reason="no way of currently testing this")
    def test_generate_random_quotes(self):
        global page
        page = HomePage(self.driver)
        for x in range(10):
            page.gimme_more_button().click()
            text = page.get_quote()
            logging.getLogger().info(text)
