from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class Ui:

    def __init__(self, driver, by, locator):
        self.locator = (by, locator)
        self.driver = driver

    def clickable(self):
        try:
            element = WebDriverWait(self.driver,10).until(
                    EC.element_to_be_clickable(self.locator))
            logging.getLogger(__name__).info(f'clickable : {bool(element)}')
            return element
        except:
            logging.getLogger(__name__).info(f'clickable : False')
            return False

    def visibility(self):
        try:
            element = WebDriverWait(self.driver,10).until(
                    EC.visibility_of_element_located(self.locator))
            logging.getLogger(__name__).info(f'visibility : {bool(element)}')
            return element
        except:
            logging.getLogger(__name__).info(f'visibility : False')
            return False

    def text(self):
        element = self.visibility()
        if element != False:
            logging.getLogger(__name__).info(f'text : {element.text}')
            return element.text
        else:
            return None

    def ele(self):
        element = self.driver.find_elements(self.locator[0], self.locator[1])
        return element
    def click(self):
        element = self.clickable()
        if element != False:
            logging.getLogger(__name__).info('click')
            element.click()
            return True
        else:
            return False

    def send_keys(self, text):
        element = self.visibility()
        if element != False:
            logging.getLogger(__name__).info('send_keys')
            element.clear()
            element.send_keys(text)
            return True
        else:
            return False
