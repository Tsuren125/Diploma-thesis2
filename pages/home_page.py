from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        'input[type="search"], input[name="search"], input#search'
    )
    SEARCH_BUTTON = (
        By.CSS_SELECTOR,
        'button[type="submit"], button.search-btn'
    )
    LOGIN_LINK = (
        By.CSS_SELECTOR,
        'a.header-auth__link, a.login-link'
    )

    def open_home(self):
        self.open('/')

    def search(self, query: str):
        el = self.wait_visible(self.SEARCH_INPUT)
        el.clear()
        el.send_keys(query)
        try:
            self.wait_clickable(self.SEARCH_BUTTON).click()
        except Exception:
            el.submit()

