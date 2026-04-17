# Проект автоматизации тестирования

## Описание
Проект содержит автотесты для двух веб-приложений:
1. **Калькулятор** (сайт: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html)
2. **Интернет-магазин SauceDemo** (сайт: https://www.saucedemo.com/)

Тесты написаны с использованием паттерна Page Object, документацией кода и Allure для формирования красивых отчетов.

## Установка зависимостей
pip install pytest allure-pytest selenium webdriver-manager

## Запуск тестов

### Для калькулятора (Chrome):
pytest test_calc.py -v --alluredir=allure-results

### Для интернет-магазина (Firefox):
pytest test_shop.py -v --alluredir=allure-results

### Запуск всех тестов:
pytest -v --alluredir=allure-results

## Формирование и просмотр Allure отчета

1. Сгенерировать отчет:
После выполнения тестов с флагом --alluredir=allure-results в папке allure-results появятся файлы с результатами.

2. Просмотреть отчет в браузере:
allure serve allure-results

После выполнения команды автоматически откроется браузер с отчетом, где можно увидеть:
- Статистику прохождения тестов
- Шаги каждого теста (с вложенными шагами)
- Декораторы: feature, story, title, description, severity, tag, link


## Примечания
- Если Firefox не открывает сайт saucedemo.com. Ошибка PR_CONNECT_RESET_ERROR связана с проблемами на стороне браузера.
- Тест для калькулятора использует Chrome, тест для магазина - Firefox (по условию задания).
"""Running pytest with args: ['-p', 'vscode_pytest', '--rootdir=c:\\Users\\Анна\\Desktop\\Python домашка\\python-curse', 'c:\\Users\\Анна\\Desktop\\Python домашка\\python-curse\\lesson_10\\tests\\test_shop.py::TestShop::test_shop']
============================= test session starts =============================
platform win32 -- Python 3.13.7, pytest-9.0.3, pluggy-1.6.0
rootdir: c:\Users\Анна\Desktop\Python домашка\python-curse
plugins: allure-pytest-2.15.3
collected 1 item

lesson_10\tests\test_shop.py .                                           [100%]

============================= 1 passed in 24.02s ==============================
Finished running tests!"""