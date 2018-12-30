from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(SeleniumDriver):
    _shopByCaIid = "nav-link-shopall"
    _submenu = "//div[@id='nav-flyout-shopAll']/div[2]//span[.=\"Women's Fashion\"]"
    _subCatLink = "//div[@id='nav-flyout-shopAll']/div[3]//span[.='Western Wear']"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def goToWesternWear(self):
        action=ActionChains(self.driver)
        # menu=self.driver.find_element_by_id(self._shopByCaIid)
        menu = self.getElement(self._shopByCaIid,"id")
        action.move_to_element(menu).perform()
        self.driver.implicitly_wait(5)
        submenu=self.driver.find_element_by_xpath(self._submenu)
        action.move_to_element(submenu).perform()
        self.driver.implicitly_wait(5)
        self.elementClick(self._subCatLink, "xpath")
        self.driver.implicitly_wait(5)
        return True
