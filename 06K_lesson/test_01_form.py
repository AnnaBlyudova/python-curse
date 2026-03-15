from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    driver = webdriver.Edge()

    driver.implicitly_wait(20)

    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    input_first_name = driver.find_element(By.NAME, "first-name")
    input_first_name.send_keys('Иван')

    input_last_name = driver.find_element(By.NAME, 'last-name')
    input_last_name.send_keys('Петров')

    input_address = driver.find_element(By.NAME, 'address')
    input_address.send_keys('Ленина, 55-3')

    input_email = driver.find_element(By.NAME, 'e-mail')
    input_email.send_keys('test@skypro.com')

    input_phone = driver.find_element(By.NAME, 'phone')
    input_phone.send_keys('+7985899998787')

    zip_code = driver.find_element(By.NAME, 'zip-code')
    assert zip_code.get_attribute('value') == '', "Поле должно быть пустым"

    input_city = driver.find_element(By.NAME, 'city')
    input_city.send_keys('Москва')

    input_country = driver.find_element(By.NAME, 'country')
    input_country.send_keys('Россия')

    input_position = driver.find_element(By.NAME, 'job-position')
    input_position.send_keys('QA')

    input_company = driver.find_element(By.NAME, 'company')
    input_company.send_keys('SkyPro')

    driver.find_element(By.CLASS_NAME, 'btn-outline-primary').click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )

    error_div = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in error_div.get_attribute("class"), \
        "Zip code не красный!"

    green_input = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]
    for green in green_input:
        element = driver.find_element(By.ID, green)
        assert 'alert-success' in element.get_attribute('class'), \
            f'Поле{green} не зеленое!'

    driver.quit()
