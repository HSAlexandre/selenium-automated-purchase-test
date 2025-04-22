import json
import logging

import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage

json_path = '../data/test_e2eFramework.json'

with open(json_path) as f:
    json_data = json.load(f)
    test_list = json_data["data"]

@pytest.mark.parametrize("test_item", test_list)
def test_e2e(browserInstance, test_item):

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
    loginPage = LoginPage(driver)
    shopPage = loginPage.login(test_item["userName"], test_item["userPassword"])


    # Accessing shop section
    shopPage.addto_Cart(test_item["productName"])
    checkoutPage = shopPage.goto_Checkout()

    #Confirming checkout
    checkoutPage.confirmCheckout()
    checkoutPage.chooseCountry(test_item["countryName"], test_item["partialCountryName"])
    checkoutPage.validatePurchase()
