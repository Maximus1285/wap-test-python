import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_mobile_element(self, by, value, timeout=15):
        """Helper method to find elements with a wait."""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def scroll_down(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
        except Exception as exception:
            print(f"An exception occurred while trying to scroll down: {exception}")
            raise exception

    def scroll_top(self):
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(1)
        except Exception as exception:
            print(f"An exception occurred while trying to scroll to the top: {exception}")
            raise exception

    def scroll_to_element(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        except Exception as exception:
            print(f"An exception occurred while trying to scroll to an element: {exception}")
            raise exception
