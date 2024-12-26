from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Singleton(object):
    __instance = None


    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            service = Service(executable_path=ChromeDriverManager().install())
            cls.__instance = webdriver.Chrome(service=service)
            return cls.__instance
        else:
            return cls.__instance
