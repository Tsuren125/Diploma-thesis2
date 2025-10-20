import pytest
from pages.login_page import LoginPage

@pytest.mark.ui
def test_login_page_opens(browser):
    page = LoginPage(browser)
    page.open()
    assert "Вход" in browser.title

