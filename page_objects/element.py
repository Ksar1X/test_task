

class Element:
    def __init__(self, locator):
        self.locator = locator

    def __repr__(self):
        return f"Element(locator='{self.locator}')"

    def find(self, driver):
        return driver.find_element(*self.locator)