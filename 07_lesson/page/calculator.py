from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator():
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/'
                        'slow-calculator.html')

    def set_delay(self):
        input_delay = self.driver.find_element(By.ID, 'delay')
        input_delay.clear()
        input_delay.send_keys('45')
        return self

    def add_numbers(self):
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()
        return self

    def wait_for_result(self):
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, '.screen'), '15'))
        return self

    def get_result_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.screen').text
