import pytest
from selenium import webdriver

@pytest.mark.usefixtures("setupLogin")
class BaseClassLogin:
    pass


