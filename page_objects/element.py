from tests.singleton import WebDriverSingleton


class Element:
    def __init__(self, locator: tuple):
        self.locator = locator

    def find(self):
        return WebDriverSingleton.get_driver().find_element(*self.locator)

    def click_on_element(self):
        element = self.find()
        element.click()

    def send_text(self, message):
        element = self.find()
        element.send_keys(message)

    def get_text(self):
        element = self.find()
        return element.text
