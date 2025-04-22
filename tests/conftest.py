import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import tempfile

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    user_data_dir = tempfile.mkdtemp()

    service = Service()
    logging.info("Initializing Webdriver")
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options,service=service)
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(service=service)
    elif browser_name == 'edge':
        driver = webdriver.Edge(service=service)
    else:
        raise ValueError(f"Browsr not supported: {browser_name}")

    driver.maximize_window()
    driver.implicitly_wait(4)
    yield driver
    logging.info("Closing browser")
    driver.close()