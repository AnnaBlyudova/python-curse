from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure


class Card():
    """Класс для работы со страницей корзины"""
    def __init__(self, driver) -> None:
        self.driver = driver

    @allure.step('Нажать кнопку Checkout')
    def click_checkout(self) -> 'Card':
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'checkout'))).click()
        return self
