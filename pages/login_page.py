from selenium.webdriver.common.by import By
from .base_page import BasePage




class LoginPage(BasePage):
EMAIL = (By.CSS_SELECTOR, 'input[type="email"], input[name="email"], input[name="LOGIN"]')
PASSWORD = (By.CSS_SELECTOR, 'input[type="password"], input[name="password"], input[name="PASSWORD"]')
SUBMIT = (By.CSS_SELECTOR, 'button[type="submit"], button.auth-button')
USER_INDICATOR = (By.CSS_SELECTOR, '.user-name, .header-user__name')


def open_login(self):
self.open('/auth/')


def login(self, email: str, password: str):
self.wait_visible(self.EMAIL).clear()
self.wait_visible(self.EMAIL).send_keys(email)
self.wait_visible(self.PASSWORD).clear()
self.wait_visible(self.PASSWORD).send_keys(password)
self.wait_clickable(self.SUBMIT).click()


def is_logged_in(self) -> bool:
try:
self.wait_visible(self.USER_INDICATOR, timeout=5)
return True
except Exception:
return False
