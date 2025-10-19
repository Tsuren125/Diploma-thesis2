from selenium.webdriver.common.by import By
from .base_page import BasePage




class ProductPage(BasePage):
ADD_TO_CART = (By.CSS_SELECTOR, 'button.add-to-cart, button.basket-btn, .buy-button')
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h1, .product-title')


def add_to_cart(self):
self.wait_clickable(self.ADD_TO_CART).click()


def get_title(self):
return self.wait_visible(self.PRODUCT_TITLE).text
