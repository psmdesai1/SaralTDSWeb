from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    HP = (By.CSS_SELECTOR, "a[class='ctl00_mnuTDS_1 ctl00_mnuTDS_3']")



    def home(self):
        return self.driver.find_element(*HomePage.HP)