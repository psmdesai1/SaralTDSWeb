from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    FY = (By.XPATH,"//select[@id='ddlFinYear']")
    UN = (By.ID, "txtUsername")
    PW = (By.ID, "txtPassword")
    LoginBtn = (By.ID, "btnLogin")
    FilterBranch = (By.ID, "txtSearch")
    SelectBranch = (By.XPATH, "//*[@id='lstBranches']/option")
    SelectBtn = (By.ID, "btnSelect")

    def finyear(self):
        return self.driver.find_element(*LoginPage.FY)

    def username(self):
        return self.driver.find_element(*LoginPage.UN)

    def password(self):
        return self.driver.find_element(*LoginPage.PW)

    def loginbutton(self):
        return self.driver.find_element(*LoginPage.LoginBtn)

    def typebranch(self):
        return self.driver.find_element(*LoginPage.FilterBranch)

    def selectbranch(self):
        return self.driver.find_element(*LoginPage.SelectBranch)

    def selectclick(self):
        return self.driver.find_element(*LoginPage.SelectBtn)
