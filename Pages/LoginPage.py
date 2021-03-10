from Pages.BasePage import BasePage
from Pages.components.HeaderMenu import HeaderMenu
from selenium.webdriver.common.by import By
from Pages.Ui import Ui


class LoginPage(BasePage, HeaderMenu):
    def input_email(self):
        return Ui(self.driver, By.ID, 'email')

    def input_password(self):
        return Ui(self.driver, By.ID, 'password')

    def login_button(self):
        return Ui(self.driver, By.ID, 'submit')

    def login_account(self, email, password):
        self.input_password().send_keys(password)
        self.input_email().send_keys(email)
        self.login_button().click()
        from Pages.TimelinePage import TimelinePage
        return TimelinePage(self.driver)
