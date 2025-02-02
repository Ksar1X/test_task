from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import threading

class WebDriverSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(WebDriverSingleton, cls).__new__(cls)
                options = Options()
                options.add_argument("--start-maximized")
                service = Service(executable_path=ChromeDriverManager().install())
                cls._instance.driver = webdriver.Chrome(service=service, options=options)
                cls._instance.driver.implicitly_wait(10)
                cls._instance.wait = WebDriverWait(cls._instance.driver, 10)
                cls._instance.action = ActionChains(cls._instance.driver)
            return cls._instance

    @staticmethod
    def get_driver():
        return WebDriverSingleton()._instance.driver

    @staticmethod
    def quit_driver():
        if WebDriverSingleton._instance:
            WebDriverSingleton._instance.driver.quit()
            WebDriverSingleton._instance = None

    @staticmethod
    def wait_for_element(by, value, condition=EC.presence_of_element_located):
        return WebDriverSingleton._instance.wait.until(condition((by, value)))







