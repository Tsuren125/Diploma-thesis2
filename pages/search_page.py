from selenium.webdriver.common.by import By
from .base_page import BasePage




class SearchPage(BasePage):
PRODUCT_CARD = (By.CSS_SELECTOR, '.product-card, .product, .catalog-item')
PRODUCT_TITLE = (By.CSS_SELECTOR, '.product-title, .product-name, .catalog-item__title')


def get_results(self):
return self.finds(self.PRODUCT_CARD)


def open_first_result(self):
cards = self.get_results()
if not cards:
raise AssertionError('Search returned no results')
cards[0].click()
