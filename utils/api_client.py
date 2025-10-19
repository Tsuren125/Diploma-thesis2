from urllib.parse import urljoin
import requests
from data.config import API_BASE, BASE_URL


class ApiClient:
    """Простой HTTP клиент для обращений к фронтенду/бэкенду сайта.

    Если у сайта есть официальный API — укажи его в API_BASE_URL в .env.
    """

    def __init__(self, base_url: str | None = None):
        if base_url:
            self.base_url = base_url.rstrip('/') + '/'
        elif API_BASE:
            self.base_url = API_BASE.rstrip('/') + '/'
        else:
            self.base_url = BASE_URL.rstrip('/') + '/'
        self.session = requests.Session()

    def _url(self, path: str) -> str:
        return urljoin(self.base_url, path.lstrip('/'))

    def get(self, path: str, **kwargs):
        return self.session.get(self._url(path), **kwargs)

    def post(self, path: str, json=None, data=None, **kwargs):
        return self.session.post(self._url(path), json=json, data=data, **kwargs)

    def put(self, path: str, json=None, **kwargs):
        return self.session.put(self._url(path), json=json, **kwargs)

    def delete(self, path: str, **kwargs):
        return self.session.delete(self._url(path), **kwargs)
