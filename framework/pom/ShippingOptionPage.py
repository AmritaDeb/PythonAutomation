from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select

class ShippingOptionPage(SeleniumDriver):
    _continueCheckout="(//input[@type='submit' and @value='Continue'])[1]"
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def continueCheckout(self):
        self.elementClick(self._continueCheckout,"xpath")
        self.driver.implicitly_wait(10)
        return True

