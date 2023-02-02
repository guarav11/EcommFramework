from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        serv_obj = Service("C:\\Selenium Browser Drivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
    elif browser=='firefox':
        serv_obj = Service("C:\\Selenium Browser Drivers\\firefoxdriver.exe")
        driver = webdriver.Firefox(service=serv_obj)
    else:
        serv_obj = Service("C:\\Selenium Browser Drivers\\Iedriver.exe")
        driver = webdriver.Ie(service=serv_obj)

    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


################ PyTest HTML Report ################
# def test_metadata(metadata):
#     assert 'metadata' in metadata['Plugins']

# It is hook for adding Environment info to HTML Report
def pytest_configure(config):
  if hasattr(config, '_metadata'):
      config._metadata['Project Name'] = 'nop Commerce'   # these are additional info we want to add in out html reports
      config._metadata['Module Name'] = 'Customers'      # these are additional info we want to add in out html reports
      config._metadata['Tester'] = 'Gaurav'         # these are additional info we want to add in out html reports


# It is hook for adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop Commerce'    # these are additional info we want to add in out html reports
#     config._metadata['Module Name'] = 'Customers'    # these are additional info we want to add in out html reports
#     config._metadata['Tester'] = 'Gaurav'    # these are additional info we want to add in out html reports

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

