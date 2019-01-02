from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(SeleniumDriver):
    _signInMenu = "//div[@id='nav-tools']/a/span[2]"
    _signInBTN = "//div[@id='nav-flyout-yourAccount']//span[.='Sign in']"
    _shopByCaIid = "nav-link-shopall"
    _submenuWomen = "//div[@id='nav-flyout-shopAll']/div[2]//span[.=\"Women's Fashion\"]"
    _subCatLinkWomen = "//div[@id='nav-flyout-shopAll']/div[3]//span[.='Western Wear']"
    _submenuAlexa = "//div[@id='nav-flyout-shopAll']/div[2]//span[.='Echo & Alexa']"
    _subCatLinkAlexa = "//div[@id='nav-flyout-shopAll']/div[3]//span[.='Amazon Echo']"


    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
    def goToLogin(self):
        action = ActionChains(self.driver)
        menu = self.getElement(self._signInMenu, "xpath")
        action.move_to_element(menu).perform()
        self.driver.implicitly_wait(5)
        self.elementClick(self._signInBTN,"xpath")
        self.driver.implicitly_wait(5)
        return True

    def goToWesternWear(self):
        action=ActionChains(self.driver)
        # menu=self.driver.find_element_by_id(self._shopByCaIid)
        menu = self.getElement(self._shopByCaIid,"id")
        action.move_to_element(menu).perform()
        self.driver.implicitly_wait(5)
        submenu=self.driver.find_element_by_xpath(self._submenuWomen)
        action.move_to_element(submenu).perform()
        self.driver.implicitly_wait(5)
        self.elementClick(self._subCatLinkWomen, "xpath")
        self.driver.implicitly_wait(5)
        return True

    def goToAmazonEcho(self):
        action = ActionChains(self.driver)
        menu = self.getElement(self._shopByCaIid, "id")
        action.move_to_element(menu).perform()
        self.driver.implicitly_wait(5)
        submenu = self.driver.find_element_by_xpath(self._submenuAlexa)
        action.move_to_element(submenu).perform()
        self.driver.implicitly_wait(5)
        self.elementClick(self._subCatLinkAlexa, "xpath")
        self.driver.implicitly_wait(5)
        return True

