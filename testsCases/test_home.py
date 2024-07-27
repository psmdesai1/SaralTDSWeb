from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):


    def test_home(self):
        hp = HomePage(self.driver)
        hp.home().click()