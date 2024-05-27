from selenium import webdriver
import pytest



@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver=webdriver.Chrome()
    elif browser == 'firefox':
        driver=webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser): # gets value from command line works as hook
    parser.addoption("--browser")


#return browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# hook for adding environment info to Html report


