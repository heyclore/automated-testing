from selenium.webdriver.common.by import By
from Pages.Ui import Ui


class Home:

    def home_menu(self):
        return Ui(self.driver, By.XPATH,
                '//*[@id="app"]/nav/div/div[1]/ul/li[1]/a')

    def home_menu_click(self):
        self.home_menu().click()
        from Pages.HomePage import HomePage
        return HomePage(self.driver)

class Timeline:

    def timeline_menu(self):
        return Ui(self.driver, By.XPATH,
                '//*[@id="app"]/nav/div/div[1]/ul/li[2]/a')

    def timeline_menu_click(self):
        self.timeline_menu().click()
        from Pages.TimelinePage import TimelinePage
        return TimelinePage(self.driver)

class Register:

    def register_menu(self):
        return Ui(self.driver, By.XPATH,
                '//*[@id="navbarSupportedContent"]/ul/li[2]/a')

    def register_menu_click(self):
        self.register_menu().click()
        from Pages.RegisterPage import RegisterPage
        return RegisterPage(self.driver)

class Login:

    def login_menu(self):
        return Ui(self.driver, By.XPATH,
                '//*[@id="navbarSupportedContent"]/ul/li[1]/a')

    def login_menu_click(self):
        self.login_menu().click()
        from Pages.LoginPage import LoginPage
        return LoginPage(self.driver)

class Logout:

    def logout_menu(self):
        return Ui(self.driver, By.XPATH,
                '//*[@id="navbarSupportedContent"]/ul/li[2]/a')

    def logout_menu_click(self):
        self.logout_menu().click()
        from Pages.HomePage import HomePage
        return HomePage(self.driver)

class Account:

    def account_menu(self):
        return Ui(self.driver, By.XPATH,
                '//*[@id="navbarSupportedContent"]/ul/li[1]/a')

    def account_menu_click(self):
        self.login_menu().click()
        from Pages.LoginPage import LoginPage
        return LoginPage(self.driver)

class HeaderMenu(Home, Timeline, Register, Login, Logout, Account):
    pass
