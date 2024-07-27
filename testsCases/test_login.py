from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from selenium import webdriver
import pytest

from utilities.BaseClassLogin import BaseClassLogin


class TestLoginPage(BaseClassLogin):

    def test_finyear(self):
        lp = LoginPage(self.driver)
        lp.finyear()

    def test_username(self):
        un = LoginPage(self.driver)
        un.username().send_keys("admin")

    def test_password(self):
        pw = LoginPage(self.driver)
        pw.password().send_keys("admin@009")

    def test_loginbtn(self):
        lb = LoginPage(self.driver)
        lb.loginbutton().click()

    def test_typebranch(self):
        tb = LoginPage(self.driver)
        tb.typebranch().send_keys("Head office")

    def test_selectbranch(self):
        sb = LoginPage(self.driver)
        sb.selectbranch().click()

    def test_selectclick(self):
        sbt = LoginPage(self.driver)
        sbt.selectclick().click()
