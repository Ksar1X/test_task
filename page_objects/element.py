from tests.singleton import WebDriverSingleton


class Element:
    def __init__(self, locator: tuple):
        self.locator = locator

    def find(self):
        return WebDriverSingleton.get_driver().find_element(*self.locator)

    def click(self):
        element = self.find()
        return element.click()

    def send(self, message):
        element = self.find()
        return element.send_keys(message)

    def get_text(self):
        element = self.find()
        return element.text