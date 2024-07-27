from time import sleep

from selenium.webdriver import ActionChains
from pageObjects.NonempPage import NonempPage
from utilities.BaseClass import BaseClass


class TestNonempPage(BaseClass):

    def test_master(self):
        act = ActionChains(self.driver)
        ne = NonempPage(self.driver)
        ne.master()
        act.move_to_element(ne.master()).perform()
    """
    def test_deduc(self):
        act = ActionChains(self.driver)
        de = NonempPage(self.driver)
        de.deduc()
        act.move_to_element(de.deduc()).perform()
        de.deduc().click()
    """
    def test_nonemp(self):
        act = ActionChains(self.driver)
        np = NonempPage(self.driver)
        np.nonemp()
        act.move_to_element(np.nonemp()).perform()
        np.nonemp().click()

    def test_name(self):
        nm = NonempPage(self.driver)
        nm.name().send_keys("Non Employee 1")

    def test_state(self):
        st = NonempPage(self.driver)
        st.state().send_keys("KARNATAKA")

    def test_custid(self):
        cu = NonempPage(self.driver)
        cu.custid().send_keys("12346")

    def test_panref(self):
        pr = NonempPage(self.driver)
        pr.panref().send_keys("BAQCJ1235G")

    def test_save(self):
        sa = NonempPage(self.driver)
        sa.save().click()
        # alrt = self.driver.switch_to.alert
        # alrt.accept()
        sleep(3)

