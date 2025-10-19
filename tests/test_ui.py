import pytest
import allure
from data.test_data import TEST_USER, SEARCH_QUERY
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage




@allure.feature('UI')
@pytest.mark.ui
def test_search_and_open_product(home_page, base_url):
"""1. Поиск книги и открытие первой карточки"""
home_page.open('/')
home_page.search(SEARCH_QUERY)
search = SearchPage(home_page.driver, base_url)
search.open_first_result()
prod = ProductPage(home_page.driver, base_url)
title = prod.get_title()
assert title and len(title) > 0




@pytest.mark.ui
def test_add_product_to_cart(home_page, base_url):
"""2. Добавление товара в корзину и проверка корзины"""
home_page.open('/')
home_page.search(SEARCH_QUERY)
search = SearchPage(home_page.driver, base_url)
search.open_first_result()
prod = ProductPage(home_page.driver, base_url)
prod.add_to_cart()
cart = CartPage(home_page.driver, base_url)
cart.open_cart()
items = cart.get_items()
assert len(items) > 0




@pytest.mar
