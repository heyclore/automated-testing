from Pages.BasePage import BasePage
from Pages.components.HeaderMenu import HeaderMenu
from selenium.webdriver.common.by import By
from Pages.Ui import Ui


class TimelinePage(BasePage, HeaderMenu):
    def list_user(self):
        foo =  Ui(self.driver, By.XPATH,
                '//*[@id="app"]/main/div[2]/div/div[*]/a').ele()
        bar = [x.text for x in foo]
        return bar
