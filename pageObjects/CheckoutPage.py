from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.confirmCheckoutButton = (By.XPATH, "//button[@class='btn btn-success']")
        self.countrySearch = (By.ID, "country")
        self.alertSuccess = (By.CLASS_NAME, "alert-success")
        self.termCheckbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.purchaseButton = (By.CSS_SELECTOR, "[type='submit']")

    def confirmCheckout(self):
        # Click the checkout button and confirm checkout
        self.driver.find_element(*self.confirmCheckoutButton).click()

    def chooseCountry(self, countryName, partialCountryName):


        # Select "UK" country
        self.driver.find_element(*self.countrySearch).send_keys(partialCountryName)
        wdw = WebDriverWait(self.driver, 10)
        wdw.until(EC.presence_of_element_located((By.LINK_TEXT, countryName)))
        self.driver.find_element(By.LINK_TEXT, countryName).click()

        # Click on "Agree terms and conditions"
        self.driver.find_element(*self.termCheckbox).click()

        # Complete purchase
        self.driver.find_element(*self.purchaseButton).click()

    def validatePurchase(self):
        # Check for Success alert
        try:
            successText = self.driver.find_element(*self.alertSuccess).text
            return "Success! Thank you!" in successText
        except Exception as e:
            print(f"Error while completing purchase: {e}")
            return False