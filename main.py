from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep
import tempfile
import logging

#functional steps
'''

'''

#loggin config
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


#locators
country = (By.LINK_TEXT, "United Kingdom")

def setup_driver(user_data_dir=None):
    options = Options()

    if user_data_dir:
        options.add_argument(f"user-data-dir={user_data_dir}")

    try:
        logging.info("Initializing Webdriver")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(options=options, service=service)
        driver.maximize_window()
        driver.implicitly_wait(4)
        return driver

    except Exception as e:
        logging.error(f"ERROR: Failed to initialize Webdriver: {e}")
        raise

def addto_cart(driver, url):

    try:

        #Accessing website
        driver.get(url)

        #Acessing shop section
        driver.find_element(By.LINK_TEXT, 'Shop').click()

        products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        #Search for "Blackberry" in all products
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                logging.info("Blackberry found")
                product.find_element(By.XPATH, "div/button").click()

        #Click the checkout button and confirm checkout
        driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        logging.info("Checkout confirmed")

        #Select "UK" country
        driver.find_element(By.ID, "country").send_keys("united")
        wdw = WebDriverWait(driver, 10)
        wdw.until(EC.presence_of_element_located(country))
        driver.find_element(By.LINK_TEXT, "United Kingdom").click()
        logging.info("UK country selected")

        #Click on "Agree terms and conditions"
        driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

        #Complete purchase
        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        logging.info("Completing purchase")

        #Check for Success alert
        successText = driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in successText
        logging.info("PASS: Purchase confirmed")

    except TimeoutException as e:
        logging.error(f'TIMEOUT: Failed to load or locate element: {e}')
        return None
    except NoSuchElementException as e:
        logging.error(f'NOT FOUND: Failed to locate element: {e}')
        return None
    except AssertionError as e:
        logging.error(f'ASSET ERROR: Purchase no completed successfully: {e}')
        return None

    finally:
        logging.info("ALL TESTS PASSED!")
        logging.info("Closing browser")
        driver.quit()

def main():

    #Script config
    url = "https://rahulshettyacademy.com/angularpractice/"
    user_data_dir = tempfile.mkdtemp()
    driver = None

    #Creating Chrome driver instance
    driver = setup_driver(user_data_dir)

    #Initializing function to follow E2E functional testing
    addto_cart(driver, url)

if __name__ == "__main__":
    main()
