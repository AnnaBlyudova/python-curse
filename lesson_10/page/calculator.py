from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Calculator():
    """Класс для работы с калькулятором на сайте bonigarcia.dev."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        Args:
            driver: Экземпляр WebDriver для управления браузером
        """
        self.driver = driver
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/'
                        'slow-calculator.html')

    @allure.step('Установить задержку 45 секунд')
    def set_delay(self) -> 'Calculator':
        """
        Устанавливает задержку 45 секунд перед вычислением.

        Returns:
            Calculator: Возвращает экземпляр
            текущего класса для цепочки вызовов
        """
        input_delay = self.driver.find_element(By.ID, 'delay')
        input_delay.clear()
        input_delay.send_keys('45')
        return self

    @allure.step('Решить пример 7 + 8')
    def add_numbers(self) -> 'Calculator':
        """
        Выполняет сложение 7 + 8, нажимая последовательно кнопки: 7, +, 8, =.

        Returns:
            Calculator: Возвращает экземпляр
            текущего класса для цепочки вызовов
        """
        with allure.step('Нажать кнопку 7'):
            self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        with allure.step('Нажать кнопку +'):
            self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        with allure.step('Нажать кнопку 8'):
            self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        with allure.step('Нажать кнопку ='):
            self.driver.find_element(By.XPATH, "//span[text()='=']").click()
        return self

    @allure.step('Ожидать результат 15 на экране')
    def wait_for_result(self) -> 'Calculator':
        """
        Ожидает появления результата 15 на экране калькулятора (до 50 секунд).

        Returns:
            Calculator: Возвращает экземпляр
            текущего класса для цепочки вызовов
        """
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, '.screen'), '15'))
        return self

    @allure.step('Получить результат вычисления с экрана калькулятора')
    def get_result_text(self) -> str:
        """
        Получает текст с экрана калькулятора.

        Returns:
            str: Текст, отображаемый на экране калькулятора
        """
        return self.driver.find_element(By.CSS_SELECTOR, '.screen').text
