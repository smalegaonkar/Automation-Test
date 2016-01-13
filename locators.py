from selenium.webdriver.common.by import By

"""1. A class for main page locators. """
class MainPageLocators(object):
    COMPANY = (By.ID, "menu-item-4286")
    MANAGEMENT = "Management"

"""1. A class for Management page locators. """
class ManagementPageLocators(object):
    BIO = (By.ID, "content")
    h3XPATH = '//*[@class="container"]/div[2]/div[2]/h3'
    pXPATH = '//*[@class="container"]/div[2]/div[2]/p[%d]'
