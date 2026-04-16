from selenium.webdriver.common.by import By
import allure


class CheckoutPage():
    """Класс для работы со страницей оформления заказа"""
    def __init__(self, driver) -> None:
        self.driver = driver

    @allure.step(
        'заполнение формы данными имя {first_name}, '
        'фамилия {last_name}, индекс {postal_code}'
    )
    def adress(self, first_name: str, last_name: str, postal_code: str
               ) -> None:
        with allure.step('Ввод имени '):
            self.driver.find_element(By.ID, 'first-name').send_keys(first_name)

        with allure.step('Ввод фамилии'):
            self.driver.find_element(By.ID, 'last-name').send_keys(last_name)

        with allure.step('Ввод почтового индекса'):
            self.driver.find_element(By.ID, 'postal-code').send_keys(
                postal_code)

        with allure.step('Нажать кнопку "Continue"'):
            self.driver.find_element(By.ID, 'continue').click()

    @allure.step('Получение итоговой стоимости заказа')
    def get_total(self) -> str:
        return self.driver.find_element(
            By.CSS_SELECTOR, '.summary_total_label').text
