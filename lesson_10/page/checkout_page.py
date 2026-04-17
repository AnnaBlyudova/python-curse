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

    def adress(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ) -> None:
        """
        Заполняет форму оформления заказа данными покупателя
        и нажимает Continue.
        """
        with allure.step('Ввод имени'):
            self.driver.find_element(By.ID, 'first-name').send_keys(first_name)
        with allure.step('Ввод фамилии'):
            self.driver.find_element(By.ID, 'last-name').send_keys(last_name)
        with allure.step('Ввод почтового индекса'):
            self.driver.find_element(By.ID, 'postal-code').send_keys(
                postal_code
            )
        with allure.step('Нажать кнопку Continue'):
            self.driver.find_element(By.ID, 'continue').click()

    def get_total(self) -> str:
        """
        Получает итоговую стоимость заказа.

        Returns:
            str: Текст с итоговой стоимостью
        """
        return self.driver.find_element(
            By.CSS_SELECTOR, '.summary_total_label'
        ).text
