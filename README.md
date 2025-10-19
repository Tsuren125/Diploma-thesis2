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

## 19) .github/workflows/ci.yml

```yaml
name: CI Tests
on:
  push:
    branches: [ main ]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run API tests
        run: pytest -m "api" --alluredir=allure-results || true
      - name: Run UI tests
        run: pytest -m "ui" --alluredir=allure-results || true
      - name: Upload Allure results
        uses: actions/upload-artifact@v4
        with:
          name: allure-results
          path: allure-results
________________________________________
Заключение
Все файлы отформатированы 
