from selenium.webdriver.common.by import By

class NonempPage:

    def __init__(self,driver):
        self.driver = driver

    Masters = (By.XPATH, "//*[@id='ctl00_mnuTDSn3']/td/table/tbody/tr/td[1]/a")
    # Dedu = (By.XPATH, "//a[.='Deductor']")
    NonEmplo = (By.XPATH,"/html/body/form/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr/td/div[3]/table/tbody/tr[5]/td/table/tbody/tr/td/a")
    Name = (By.NAME, "ctl00$contentPlaceHolderBody$txtNonEmployeeName")
    State = (By.NAME, "ctl00$contentPlaceHolderBody$cmbState")
    CustID = (By.NAME, "ctl00$contentPlaceHolderBody$txtReferenceNo")
    PANRef = (By.NAME, "ctl00$contentPlaceHolderBody$txtPanReference")
    Save = (By.XPATH, "//*[@id='ctl00_contentPlaceHolderBody_btnSave']")

    def master(self):
        return self.driver.find_element(*NonempPage.Masters)

    # def deduc(self):
    #     return self.driver.find_element(*NonempPage.Dedu)

    def nonemp(self):
        return self.driver.find_element(*NonempPage.NonEmplo)

    def name(self):
        return self.driver.find_element(*NonempPage.Name)

    def state(self):
        return self.driver.find_element(*NonempPage.State)

    def custid(self):
        return self.driver.find_element(*NonempPage.CustID)

    def panref(self):
        return self.driver.find_element(*NonempPage.PANRef)

    def save(self):
        return self.driver.find_element(*NonempPage.Save)
