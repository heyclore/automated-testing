from Pages.BasePage import BasePage
from Pages.components.HeaderMenu import HeaderMenu
from selenium.webdriver.common.by import By
from Pages.Ui import Ui


class HomePage(BasePage, HeaderMenu):

    def quote(self):
        return Ui(self.driver, By.ID, 'quote')

    def author(self):
        return Ui(self.driver, By.ID, 'author')

    def user(self):
        return Ui(self.driver, By.ID, 'user')

    def gimme_more_button(self):
        return Ui(self.driver, By.XPATH,
                '//*[@id="app"]/main/div/div/div/div[2]/button')

    def get_quote(self):
        quote =  self.quote().text()
        author =  self.author().text()
        user =  self.user().text()
        return f"quote : '{quote}', author: {author}, user: {user}"
