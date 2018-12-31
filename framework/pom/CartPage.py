from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select

class CartPage(SeleniumDriver):
    _checkoutName = "proceedToCheckout"
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def proceedToCheckout(self):
        self.elementClick(self._checkoutName,"name")
        self.driver.implicitly_wait(10)
        return True

