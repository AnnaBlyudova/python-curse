import allure
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from page.autoriz import LoginPage
from page.products import Products
from page.cart import Card
from page.checkout_page import CheckoutPage
import pytest
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@allure.feature('Интернет-магазин SauceDemo')
@allure.story('Оформление заказа')
class TestShop:

    @pytest.fixture()
    def driver(self) -> WebDriver:
        """
        Фикстура для инициализации и закрытия драйвера Firefox.

        Returns:
            WebDriver: Экземпляр драйвера Firefox
        """
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.id("SHOP-1")
    @allure.feature("Оформление заказа")
    @allure.story("Добавление товаров и покупка")
    @allure.title("Тест оформления заказа с добавлением товаров")
    @allure.description("""
        Тест проверяет оформление заказа в интернет-магазине SauceDemo:
        1. Авторизация как standard_user
        2. Добавление товаров: Backpack, Bolt T-Shirt, Onesie
        3. Переход в корзину и нажатие Checkout
        4. Заполнение формы данными покупателя
        5. Проверка итоговой суммы: $58.29
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('smoke', 'regression')
    @allure.link('https://www.saucedemo.com/', name='SauceDemo')
    def test_shop(self, driver: WebDriver) -> None:
        """
        Тест проверки оформления заказа в интернет-магазине.

        Args:
            driver: Экземпляр WebDriver
        """
        with allure.step('Открыть страницу авторизации и выполнить вход'):
            name = LoginPage(driver)
            name.autorization('standard_user', 'secret_sauce')

        with allure.step('Добавить товары в корзину'):
            product = Products(driver)
            product.add_to_card()

        with allure.step('Нажать кнопку Checkout'):
            cart = Card(driver)
            cart.click_checkout()

        with allure.step('Заполнить форму данными покупателя'):
            full_form = CheckoutPage(driver)
            full_form.adress('Анна', 'Блюдова', '085013')

        with allure.step('Проверить итоговую стоимость заказа'):
            result_price = full_form.get_total()
            assert '$58.29' in result_price, f'Ожидалось "$58.29", получено "{result_price}"'
