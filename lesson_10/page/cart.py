from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Card():
    """Класс для работы со страницей корзины."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.

        Args:
            driver: Экземпляр WebDriver для управления браузером
        """
        self.driver = driver

    @allure.step('Нажать кнопку Checkout')
    def click_checkout(self) -> 'Card':
        """
        Нажимает кнопку Checkout для перехода к оформлению заказа.

        Returns:
            Card: Возвращает экземпляр текущего класса для цепочки вызовов
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'checkout'))).click()
        return self
