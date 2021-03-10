from Pages.BasePage import BasePage
from Pages.components.HeaderMenu import HeaderMenu
from selenium.webdriver.common.by import By
from Pages.Ui import Ui


class RegisterPage(BasePage, HeaderMenu):

    def input_username(self):
        return Ui(self.driver, By.ID, 'username')

    def input_email(self):
        return Ui(self.driver, By.ID, 'email')

    def input_password(self):
        return Ui(self.driver, By.ID, 'password')

    def input_confirm_password(self):
        return Ui(self.driver, By.ID, 'confirm_password')

    def submit_button(self):
        return Ui(self.driver, By.ID, 'submit')

    def register_account(self, username, email, password,
            confirm_password):
        self.input_username().send_keys(username)
        self.input_email().send_keys(email)
        self.input_password().send_keys(password)
        self.input_confirm_password().send_keys(confirm_password)
        self.submit_button().click()
        from Pages.TimelinePage import TimelinePage
        return TimelinePage(self.driver)
