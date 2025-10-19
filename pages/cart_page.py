from selenium.webdriver.common.by import By
from .base_page import BasePage




class CartPage(BasePage):
CHECKOUT_BTN = (By.CSS_SELECTOR, 'a.checkout, button.checkout')
CART_ITEMS = (By.CSS_SELECTOR, '.cart-item, .basket-list__item')


def open_cart(self):
self.open('/cart')


def get_items(self):
return self.finds(self.CART_ITEMS)
