import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseTest:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        mobile_emulation = { "deviceName": "iPhone X" }
        # Set up Chrome options
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_experimental_option("mobileEmulation", mobile_emulation)

        # Initialize the WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        yield
        self.driver.quit()

    def find_mobile_element(self, by, value, timeout=15):
        """Helper method to find elements with a wait."""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))
