import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.confirmCheckoutButton = (By.XPATH, "//button[@class='btn btn-success']")
        self.countrySearch = (By.ID, "country")
        self.foundCountry = (By.LINK_TEXT, "United Kingdom")
        self.alertSuccess = (By.CLASS_NAME, "alert-success")
        self.termCheckbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.purchaseButton = (By.CSS_SELECTOR, "[type='submit']")

    def confirmCheckout(self):
        # Click the checkout button and confirm checkout
        self.driver.find_element(*self.confirmCheckoutButton).click()
        logging.info("Checkout confirmed")

    def chooseCountry(self, countryName):
        self.countryName = countryName

        # Select "UK" country
        self.driver.find_element(*self.countrySearch).send_keys(countryName)
        wdw = WebDriverWait(self.driver, 10)
        wdw.until(EC.presence_of_element_located(self.foundCountry))
        self.driver.find_element(*self.foundCountry).click()
        logging.info("UK country selected")

        # Click on "Agree terms and conditions"
        self.driver.find_element(*self.termCheckbox).click()

        # Complete purchase
        self.driver.find_element(*self.purchaseButton).click()
        logging.info("Completing purchase")

    def validatePurchase(self):
        # Check for Success alert
        successText = self.driver.find_element(*self.alertSuccess).text
        assert "Success! Thank you!" in successText
        logging.info("PASS: Purchase confirmed")