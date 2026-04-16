import allure
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from page.calculator import Calculator
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@allure.epic("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite('Тесты на работу калькулятора')
class TestCalculator:

    @pytest.fixture()
    def driver(self) -> WebDriver:
        """
        Фикстура для инициализации и закрытия драйвера Chrome.

        Yields:
            WebDriver: Экземпляр драйвера Chrome
        """
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.id("CALC-1")
    @allure.feature("Сложение")
    @allure.story("Сложение с задержкой")
    @allure.title("Тест сложения 7 + 8 с задержкой 45 секунд")
    @allure.description("""
        Тест проверяет сложение 7 + 8 на калькуляторе с задержкой 45 секунд.
        Ожидаемый результат: 15
    """)
    @allure.tag("smoke", "calculator")
    @allure.link(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html",
        name="Slow Calculator")
    def test_calculator(self, driver: WebDriver) -> None:
        """
        Тест проверки работы калькулятора с задержкой.

        Args:
            driver: Экземпляр WebDriver
        """
        with allure.step('Открыть страницу калькулятора и выполнить действия'):
            calc = Calculator(driver)

        with allure.step('Установить задержку 45 секунд'):
            calc.set_delay()

        with allure.step('Решить пример 7 + 8'):
            calc.add_numbers()

        with allure.step('Ожидать результат 15 на экране'):
            calc.wait_for_result()

        with allure.step('Проверить результат вычисления'):
            result_text = calc.get_result_text()
            assert result_text == '15', f'Ожидалось "15", получено "{result_text}"'
