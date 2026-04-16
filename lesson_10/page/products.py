from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Products():
    """
    Класс для работы со страницей товаров интернет-магазина.
    Содержит методы для добавления товаров в корзину и перехода в корзину.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы товаров с ожиданием загрузки.

        Args:
            driver: Экземпляр WebDriver для управления браузером
        """
        self.driver = driver
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, 'add-to-cart-sauce-labs-backpack')))

    @allure.step('Добавление товаров в корзину и переход в корзину')
    def add_to_card(self) -> 'Products':
        """
        Добавляет в корзину три товара и переходит на страницу корзины:
        - Sauce Labs Backpack
        - Sauce Labs Bolt T-Shirt
        - Sauce Labs Onesie

        Returns:
            Products: Возвращает экземпляр текущего класса для цепочки вызовов
        """
        with allure.step('Добавить Sauce Labs Backpack'):
            self.driver.find_element(
                By.ID, 'add-to-cart-sauce-labs-backpack').click()
        with allure.step('Добавить Sauce Labs Bolt T-Shirt'):
            self.driver.find_element(
                By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        with allure.step('Добавить Sauce Labs Onesie'):
            self.driver.find_element(
                By.ID, 'add-to-cart-sauce-labs-onesie').click()
        with allure.step('Перейти в корзину'):
            self.driver.find_element(
                By.CSS_SELECTOR, '.shopping_cart_link').click()
        return self
