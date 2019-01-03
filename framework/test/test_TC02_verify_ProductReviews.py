from framework.pom.HomePage import HomePage
from framework.pom.ProductDetailsPage import ProductDetailsPage
import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_productDetails(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.pdp = ProductDetailsPage(self.driver)

    @pytest.mark.run(order=1)
    def test_goToPDP(self):
        self.hp.goToAmazonEcho()
        actual=self.pdp.getAvailibilityAlexa()
        assert "In stock" in actual,"Product is not in stock"
        print("The total count of review: ",self.pdp.getReviewCount())
        print("The Review Summary: ")
        self.pdp.getReviews()



