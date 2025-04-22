import json
import logging
import pytest
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pageObjects.LoginPage import LoginPage
import allure



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
    with allure.step("Signing in"):
        loginPage = LoginPage(driver)
        shopPage = loginPage.login(test_item["userName"], test_item["userPassword"])
        assert shopPage is not None


    # Accessing shop section
    with allure.step("Adding product to cart"):
        shopPage.addto_Cart(test_item["productName"])
        checkoutPage = shopPage.goto_Checkout()
        assert checkoutPage is not None
    #Confirming checkout
    with allure.step("Confirming purchase"):
        checkoutPage.confirmCheckout()
        checkoutPage.chooseCountry(test_item["countryName"], test_item["partialCountryName"])
        result = checkoutPage.validatePurchase()
