from selenium.webdriver.common.by import By
import allure


class LoginPage():
    """Класс для работы со страницей авторизации SauceDemo"""
    def __init__(self, driver) -> None:
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/')

    @allure.step(
            'Авторизация на сайте с логином {username} и паролем {password}')
    def autorization(self, username: str, password: str) -> 'LoginPage':
        with allure.step('Ввод логина'):
            self.driver.find_element(By.ID, 'user-name').send_keys(username)
        with allure.step('Ввод пароля'):
            self.driver.find_element(By.ID, 'password').send_keys(password)
        with allure.step('Нажатие кнопки Login'):
            self.driver.find_element(By.ID, 'login-button').click()
        return self
