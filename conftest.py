import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from data.config import BASE_URL, HEADLESS
from utils.api_client import ApiClient
from pages.home_page import HomePage
from pages.login_page import LoginPage




@pytest.fixture(scope='session')
def base_url():
return BASE_URL




@pytest.fixture(scope='session')
def api_client():
return ApiClient()




@pytest.fixture
def driver():
options = webdriver.ChromeOptions()
if HEADLESS:
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
yield driver
driver.quit()




@pytest.fixture
def home_page(driver, base_url):
return HomePage(driver, base_url)




@pytest.fixture
def login_page(driver, base_url):
return LoginPage(driver, base_url)
