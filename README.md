# Автотесты для Chitai-Gorod

Проект содержит 5 UI и 5 API тестов для сайта https://www.chitai-gorod.ru

## Быстрый старт
1. Склонируйте репозиторий.
2. Создайте `.env` по образцу `.env.example`.
3. Установите зависимости:
python -m pip install -r requirements.txt 4. Запустите тесты: pytest -m “ui” pytest -m “api” 5. Посмотреть Allure отчет: allure serve allure-results ```
Примечания по локаторам
Локаторы в pages/ подобраны ориентировочно. Если тест падает — открой DevTools и скорректируй селекторы в соответствующем PageObject.

---


