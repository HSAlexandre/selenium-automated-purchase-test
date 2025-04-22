from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from pageObjects.ShopPage import ShopPage
from pageObjects.LoginPage import LoginPage


def test_e2e(browserInstance):

    # logging config
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    # locators
    country = (By.LINK_TEXT, "United Kingdom")

    # Creating Browser driver instance
    driver = browserInstance

    # Accessing website
    url = "https://rahulshettyacademy.com/loginpagePractise/"
    productName = "Blackberry"
    countryName = "United"
    driver.get(url)

    #Signing in
    loginPage = LoginPage(driver)
    shopPage = loginPage.login('rahulshettyacademy', 'learning')


    # Accessing shop section
    shopPage.addto_Cart(productName)
    checkoutPage = shopPage.goto_Checkout()

    #Confirming checkout
    checkoutPage.confirmCheckout()
    checkoutPage.chooseCountry(countryName)
    checkoutPage.validatePurchase()
