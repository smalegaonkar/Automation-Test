from selenium.webdriver.common.action_chains import ActionChains

from locators import MainPageLocators
from locators import ManagementPageLocators


"""Base class to initialize the base page that will be called from all pages"""
class BasePage(object) :
    def __init__(self, driver):
        self.driver = driver  

"""Class for Home page of BetterCloud"""
class HomePage(BasePage) :

    def hover (self) :
        element_to_hover_over = self.driver.find_element(*MainPageLocators.COMPANY);
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over);
        hover.perform();
        print "Hovered Over Company"

    def visitManagementPage(self) :
        #Move to management link and click it
        self.driver.find_element_by_partial_link_text(MainPageLocators.MANAGEMENT).click()
        print "Clicked Management link"


"""Class for Management Page """           
class ManagementPage(BasePage) :

    def scrapeLastWord (self) :
        endPunctuations = set('.?!')
        self.lastWords = []

        #Iterate through Heading of David Hardwick
        h3Text = self.driver.find_element_by_xpath(ManagementPageLocators.h3XPATH).text
        for word in h3Text.split(' '):
                 if endPunctuations & set(word):
                     word = word.strip()
                     word = word[:-1]
                     self.lastWords.append(word)
                     
        #Iterate through paragraphs(total 3) of David Hardwick                    
        for i in range(1, 4):
            pXPATH = ManagementPageLocators.pXPATH % i
            paraText = self.driver.find_element_by_xpath(pXPATH).text

            #Check each word & pick the word containing an 'endPunctuations' char. Then add to array
            for word in paraText.split(' '):
                 if endPunctuations & set(word):
                     word = word.strip()
                     word = word[:-1]
                     self.lastWords.append(word)

    def sortAndPrint(self) :
        print;
        for word in sorted(self.lastWords, key=lambda k : k.lower()):
            print word
