from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class LoginPage():
    """
    Класс для работы со страницей авторизации SauceDemo.
    Содержит методы для ввода логина/пароля и нажатия кнопки входа.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы авторизации.

        Args:
            driver: Экземпляр WebDriver для управления браузером
        """
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/')

    @allure.step('Авторизация на сайте с логином {username}')
    def autorization(self, username: str, password: str) -> 'LoginPage':
        """
        Выполняет авторизацию на сайте с указанными учетными данными.

        Args:
            username: Имя пользователя (str)
            password: Пароль пользователя (str)

        Returns:
            LoginPage: Возвращает экземпляр текущего класса для цепочки вызовов
        """
        with allure.step('Ввод логина'):
            self.driver.find_element(By.ID, 'user-name').send_keys(username)
        with allure.step('Ввод пароля'):
            self.driver.find_element(By.ID, 'password').send_keys(password)
        with allure.step('Нажатие кнопки Login'):
            self.driver.find_element(By.ID, 'login-button').click()
        return self
