from selenium.webdriver.common.by import By

from pageObjects.ShopPage import ShopPage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, 'username')
        self.password = (By.NAME, 'password')
        self.signInBtn = (By.ID, 'signInBtn')

    def login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.signInBtn).click()
        shopPage = ShopPage(self.driver)
        return shopPage