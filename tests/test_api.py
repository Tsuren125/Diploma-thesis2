import pytest
import allure


@allure.feature('API')
@pytest.mark.api
def test_frontend_health(api_client):
    """1. Проверяем, что главная страница доступна (200)"""
    r = api_client.get('/')
    assert r.status_code == 200


@pytest.mark.api
def test_search_endpoint(api_client):
    """2. Проверяем, что поиск возвращает 200 или 204 (если пусто)"""
    r = api_client.get('/catalog/search', params={'q': 'книга'})
    assert r.status_code in (200, 204)


@pytest.mark.api
def test_add_to_cart_api(api_client):
    """3. Проверка добавления в корзину через API (если доступно)"""
    payload = {'product_id': 1, 'quantity': 1}
    r = api_client.post('/cart/add', json=payload)
    assert r.status_code in (200, 201)


@pytest.mark.api
def test_get_cart(api_client):
    """4. Получение корзины"""
    r = api_client.get('/cart')
    assert r.status_code in (200, 204)


@pytest.mark.api
def test_unauthorized_checkout(api_client):
    """5. Попытка оформить заказ без авторизации даёт 401/403"""
    payload = {'cart_id': 1, 'payment': 'test'}
    r = api_client.post('/order/checkout', json=payload)
    assert r.status_code in (401, 403, 400)
