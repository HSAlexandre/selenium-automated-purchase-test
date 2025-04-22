from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

def test_e2e(browserInstance):

    # logging config
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    # locators
    country = (By.LINK_TEXT, "United Kingdom")

    # Creating Browser driver instance
    driver = browserInstance

    # Accessing website
    url = "https://rahulshettyacademy.com/loginpagePractise/"
    driver.get(url)

    #Signing in
    driver.find_element(By.ID, 'username').send_keys('rahulshettyacademy')
    driver.find_element(By.NAME, 'password').send_keys('learning')
    driver.find_element(By.ID, 'signInBtn').click()


    # Accessing shop section
    driver.find_element(By.LINK_TEXT, 'Shop').click()

    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    # Search for "Blackberry" in all products
    for product in products:
        productName = product.find_element(By.XPATH, "div/h4/a").text
        if productName == "Blackberry":
            logging.info("Blackberry found")
            product.find_element(By.XPATH, "div/button").click()

    # Click the checkout button and confirm checkout
    driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    logging.info("Checkout confirmed")

    # Select "UK" country
    driver.find_element(By.ID, "country").send_keys("united")
    wdw = WebDriverWait(driver, 10)
    wdw.until(EC.presence_of_element_located(country))
    driver.find_element(By.LINK_TEXT, "United Kingdom").click()
    logging.info("UK country selected")

    # Click on "Agree terms and conditions"
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

    # Complete purchase
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    logging.info("Completing purchase")

    # Check for Success alert
    successText = driver.find_element(By.CLASS_NAME, "alert-success").text
    assert "Success! Thank you!" in successText
    logging.info("PASS: Purchase confirmed")
