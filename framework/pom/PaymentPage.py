from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select

class PaymentPage(SeleniumDriver):
    _defaultPaymentOption = "//span[contains(text(),'Your saved credit and debit cards')]/../../following-sibling::div"
    _anotherPaymentOptions = "//span[contains(text(),' Another payment method')]/../../following-sibling::div"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def countNoOfDeliveryOption(self):
        self.driver.find_element_by_xpath(self._defaultPaymentOption)
        count=len(self.driver.find_elements_by_xpath(self._anotherPaymentOptions))
        return count

