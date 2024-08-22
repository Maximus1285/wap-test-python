from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.config import Config

class TwitchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.BASE_URL
        self.page_title = "Twitch"

    def load(self):
        self.driver.get(self.url)

    def is_loaded(self):
        return self.page_title in self.driver.title

    def pick_first_streamer(self):
        try:
            selected_channel = self.find_mobile_element(By.CSS_SELECTOR, "[role=list] article")
            streamer_href = selected_channel.find_element(By.CSS_SELECTOR, '.tw-link').get_attribute('href')
            selected_channel.click()
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.chat-line__message-container')))
            return streamer_href
        except Exception as exception:
            print(f"Timed out waiting for element: {exception}")
            raise exception

    def search_for(self, search_term):
        try:
            search_icon = self.find_mobile_element(By.CSS_SELECTOR, '[aria-label="Search"]')
            search_icon.click()

            search_input = self.find_mobile_element(By.CSS_SELECTOR, '[data-a-target="tw-input"]')
            search_input.send_keys(search_term)

            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.tw-link'))
            )

            selected_option = self.find_mobile_element(By.CSS_SELECTOR, '[href="/directory/category/starcraft-ii"]')
            selected_option.click()
        except Exception as exception:
            print(f"An exception occurred while trying to search for a streamer: {exception}")
            raise exception
