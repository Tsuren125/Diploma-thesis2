import os
from dotenv import load_dotenv


load_dotenv()


BASE_URL = os.getenv('BASE_URL', 'https://www.chitai-gorod.ru')
API_BASE = os.getenv('API_BASE_URL', '')
HEADLESS = os.getenv('HEADLESS', 'true').lower() in ('1', 'true', 'yes')
