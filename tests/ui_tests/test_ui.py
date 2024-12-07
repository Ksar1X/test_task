from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


def test_user_cannot_login_with_empty_fields():
    driver.get("https://thinking-tester-contact-list.herokuapp.com")
    submit_button = driver.find_element("xpath", "//button[1]")
    submit_button.click()
    error = driver.find_element("id", "error")
    assert error is not None

def test_login_user():
    driver.get("https://thinking-tester-contact-list.herokuapp.com")
    email_field = driver.find_element("xpath", "//input[@placeholder='Email']")
    email_field.send_keys("garynychxxx@gmail.com")
    password_field = driver.find_element("xpath", "//input[@placeholder='Password']")
    password_field.send_keys("raketa123")
    submit_button = driver.find_element("xpath", "//button[1]")
    submit_button.click()
    assert driver.current_url == "https://thinking-tester-contact-list.herokuapp.com/contacts"
