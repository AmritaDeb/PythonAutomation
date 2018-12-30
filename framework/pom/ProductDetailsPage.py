from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select

class ProductDetailsPage(SeleniumDriver):
    _availibility = "//h2[.='Product details']/../div/ul/li[3]/b"
    _sizeID = "native_dropdown_selected_size_name"
    _reviewId="acrCustomerReviewText"
    # _addToCartId="add-to-cart-button"
    _addToCart="//span[@id='submit.add-to-cart']"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    # def getAvailibility(self):
    #     # print(self.getElement(self._availibility,"xpath").text)
    #     print(self.driver.find_element_by_xpath(self._availibility).text)

    # def selectSize(self):
    #     size=self.getElement(self._sizeID,"id")
    #     select=Select(size)
    #     option=select.select_by_index(3)
    #     self.driver.implicitly_wait(5)

    def addToCart(self):
        self.elementClick(self._addToCart,"xpath")
        self.driver.implicitly_wait(5)
        return True
