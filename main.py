from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

import pages
from locators import MainPageLocators
from locators import ManagementPageLocators


""" Language--> Python   Version: 2.7.11
    Automation Framework used: Selenium WebDriver (Python) (Version 2.48.0)
    Design Pattern--> OOP & Page Object Design """

"""If required, code readability can be enhanced by using Geb+Spock"""

def main ():
    driver = webdriver.Firefox()
    driver.maximize_window()
    url = 'http://bettercloud.com';
    driver.get(url)

    #Make sure Main page loads successfully
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.COMPANY))
        print "Home Page Loaded Successfully"
    except:
        print "Home Page Loading ERROR";
        driver.close();
        sys.exit(0);

    homePage = pages.HomePage(driver);
    homePage.hover();
    homePage.visitManagementPage();
    
    #Make sure Management page loads successfully
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(ManagementPageLocators.BIO))
        print "Management Page Loaded Successfully"
    except:
        print "Management Page Loading ERROR"
        driver.close();
        sys.exit(0);

    managementPage = pages.ManagementPage(driver);
    managementPage.scrapeLastWord();
    managementPage.sortAndPrint();

    # close() method is used to close tab & quit() method exits entire browser
    driver.close();

if __name__ == "__main__":
    main()
