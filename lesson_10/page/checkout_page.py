from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class CheckoutPage():
    """Класс для работы со страницей оформления заказа."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа.

        Args:
            driver: Экземпляр WebDriver для управления браузером
        """
        self.driver = driver

    @allure.step('Заполнение формы данными: {first_name} {last_name}, индекс {postal_code}')
    def adress(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму оформления заказа данными покупателя и нажимает Continue.

        Args:
            first_name: Имя покупателя (str)
            last_name: Фамилия покупателя (str)
            postal_code: Почтовый индекс (str)

        Returns:
            None
        """
        with allure.step('Ввод имени'):
            self.driver.find_element(By.ID, 'first-name').send_keys(first_name)
        with allure.step('Ввод фамилии'):
            self.driver.find_element(By.ID, 'last-name').send_keys(last_name)
        with allure.step('Ввод почтового индекса'):
            self.driver.find_element(By.ID, 'postal-code').send_keys(postal_code)
        with allure.step('Нажать кнопку Continue'):
            self.driver.find_element(By.ID, 'continue').click()

    @allure.step('Получение итоговой стоимости заказа')
    def get_total(self) -> str:
        """
        Получает итоговую стоимость заказа со страницы подтверждения.

        Returns:
            str: Текст с итоговой стоимостью (например, "Total: $58.29")
        """
        return self.driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
