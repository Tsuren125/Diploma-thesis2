from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(@class,'header-search__button')]")
    BOOK_TITLES = (By.CSS_SELECTOR, ".product-card__title")

    def search_book(self, query):
        self.send_keys(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)
