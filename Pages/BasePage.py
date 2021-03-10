from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging
import time
import inspect

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def __getattribute__(self, name):
        returned = object.__getattribute__(self, name)
        if inspect.isfunction(returned) or inspect.ismethod(returned):
            if name not in ['get_text', 'click']:
                time.sleep(0.1)
                logging.getLogger(__name__).info(name)
        return returned

    def click(self, locator):
        WebDriverWait(self.driver,10).until(
                EC.visibility_of_element_located(locator)).click()

    def send_keys(self, locator, text):
        WebDriverWait(self.driver,10).until(
                EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        element = WebDriverWait(self.driver,10).until(
                EC.visibility_of_element_located(locator)).text
        logging.getLogger().info(element)
        return element

    def get_attribute(self, locator, attribute):
        text = WebDriverWait(self.driver,10).until(
                EC.visibility_of_element_located(locator)
                ).get_attribute(attribute)
        return text

    def visible(self,locator):
        element = WebDriverWait(self.driver,10).until(
                EC.visibility_of_element_located(locator))
        return bool(element)

    def get_title(self):
        title = self.driver.title
        logging.getLogger(__name__).info(f"title : '{title}'")
        return title
