import logging
from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage


class ShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.shopLink = (By.LINK_TEXT, 'Shop')
        self.productsCard = (By.XPATH, "//div[@class='card h-100']")
        self.cartButton = (By.XPATH, "div/button")
        self.checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")


    def addto_Cart(self, productName):
        self.driver.find_element(*self.shopLink).click()
        self.productName = productName

        products = self.driver.find_elements(*self.productsCard)

        # Search for "Blackberry" in all products
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == productName:
                logging.info("Blackberry found")
                product.find_element(*self.cartButton).click()

    def goto_Checkout(self):
        self.driver.find_element(*self.checkoutButton).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage