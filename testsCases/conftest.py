import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="D:/browserdrivers/chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "IE":
        print("IE driver")
    driver.get("http://laptop-nrp52uus/SaralTDS/Authentication/Login.aspx")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)




"""
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_name", action="store", default="msedge"
#     )
#
#
# @pytest.fixture(scope="class")
# def setup(request):
#     browser_name=request.config.getoption("browser_name")
#     if browser_name == "msedge":
#         driver = webdriver.Edge(executable_path="D:/browserdrivers/msedgedriver.exe")
#     elif browser_name == "chrome":
#         driver = webdriver.Chrome(executable_path="D:/browserdrivers/chromedriver.exe")
#     elif browser_name == "firefox":
#         driver = webdriver.Firefox(executable_path="D:/browserdrivers/geckodriver.exe")
#     driver.get("http://laptop-nrp52uus/SaralTDS/Authentication/Login.aspx")
#     driver.maximize_window()
#     driver.find_element("id", "txtUsername").send_keys("admin")
#     driver.find_element("id", "txtPassword").send_keys("admin@009")
#     driver.find_element("id", "btnLogin").click()
#     driver.find_element("id", "txtSearch").click()
#     driver.find_element("id", "txtSearch").send_keys("head office")
#     driver.find_element("xpath", "//*[@id='lstBranches']/option").click()
#     driver.find_element("id", "btnSelect").click()

#     request.cls.driver = driver
#     # yield
#     # driver.close()
"""
@pytest.fixture(scope="class")
def setupLogin(request):

    driver = webdriver.Chrome(executable_path="D:/browserdrivers/chromedriver.exe")
    driver.get("http://laptop-nrp52uus/SaralTDS/Authentication/Login.aspx")
    driver.implicitly_wait(5)
    # WebDriverWait(driver,12)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


# @pytest.fixture(scope="class")
# def setup(request):
#
#     driver = webdriver.Chrome(executable_path="D:/browserdrivers/chromedriver.exe")
#     driver.get("http://laptop-nrp52uus/SaralTDS/Authentication/Login.aspx")
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     driver.find_element("id", "txtUsername").send_keys("admin")
#     driver.find_element("id", "txtPassword").send_keys("admin@009")
#     driver.find_element("id", "btnLogin").click()
#     driver.find_element("id", "txtSearch").click()
#     driver.find_element("id", "txtSearch").send_keys("head office")
#     driver.find_element("xpath", "//*[@id='lstBranches']/option").click()
#     driver.find_element("id", "btnSelect").click()
#     request.cls.driver = driver
#     yield
#     driver.close()







