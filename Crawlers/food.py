from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from wia import Wia
from selenium.webdriver.support.ui import Select
import time


# wia = Wia()
# wia.access_token = "d_sk_ijPaZ2GTs0xrmrKu3tZu0fkp"
# deviceId = 'dev_5wrc9tH1'
# slug = 'order-pizza'
# wia.Stream.connect()
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

class FoodBot:

    # Enter Your Details below
    first_name = "Adam"
    last_name = "Kelly"
    contact_number = "8258585825"
    email_address = "gfguf@h.com"
    address = "Dogpatch Labs"
    building = "u88"
    building_num = "y8ugfy"
    street = "252982bgfyf"
    district = "gujgf"
    city = "higu"
    eircode = "igi"

    # Enter your pizza number in the javascript below (var pizzaNum)
    '''
    0 - Buffalo
    1 - Plain Cheese Pizza 
    2 - Hiwatha
    3 - Bacon Apache
    4 - The Big Chief
    5 - Hot Apache
    6 - Vegetarian
    7 - Chicken Apache
    8 - Mexican Pepper Volcano
    9 - Wigwammer
    10 - Premium Moonshine
    11 - Cajun Apache
    12 - Premium Big Buffalo
    13 - Premium Chicken Feast
    14 - Premium Taco Volcano
    15 - Premium Volcano
    16 - Apache Special

    '''
    

    def __init__(self):

        # For The Location Of The Chromedriver
        chromedriver = '../../../Chromedrivers/chromedriver_mac64/chromedriver'
        self.driver = webdriver.Chrome(chromedriver, options = options)

    def placeOrder(self):
            driver = self.driver
            driver.get('https://www.apache.ie/')

            driver.maximize_window()

            driver.execute_script("var pizzaNum = 0;")

            driver.execute_script
            (
                " var pizzaNum = 0; window.scroll(0,290); var plusBtn = document.getElementsByClassName('s4d-product-amount-plus s4d-text-color-medium'); plusBtn[6].click(); var orderBtn = document.getElementsByClassName('btn btn-primary add-menu-overview-product-button order-btn-reference'); orderBtn[pizzaNum].click();  orderBtn[8].click(); window.location.href = 'https://www.apache.ie/secure/checkout';"
            )
            # pizza = driver.find_element_by_xpath('//div[@class="s4d-menu-overview-product-btn-block"]//descendant::input[@]')

            driver.execute_script("var select = document.getElementsByClassName('btn-link selectStore-check-form-open btn-sm'); select[0].click();")

            driver.implicitly_wait(200)

            driver.find_element_by_xpath('//*[@id="SearchStoreSelector"]').send_keys(self.address + Keys.TAB + Keys.ENTER )

            driver.implicitly_wait(2000)

            results =  driver.find_elements_by_xpath('//div[@class="s4d-scroll-content"]//descendant::a[@data-store-id="82"]')
            results[0].click()
           
            print("The total number of suggestions is " + str(len(results))) 
           
            
    def inputDetails(self):
        driver = self.driver 
        time.sleep(2)
        first_name = driver.find_element_by_id('CustomerData_Firstname')
        first_name.send_keys(self.first_name + Keys.TAB)

        last_name = driver.find_element_by_id('CustomerData_Lastname')
        last_name.send_keys(self.last_name + Keys.TAB)

        phone_num = driver.find_element_by_id('CustomerData_Phonenumber')
        phone_num.send_keys(self.contact_number + Keys.TAB)

        email_address = driver.find_element_by_id('CustomerData_Emailaddress')
        email_address.send_keys(self.email_address + Keys.TAB)

        address = driver.find_element_by_id('CustomerData_AddressViewModel_SuggestionBox')
        address.send_keys(self.address + Keys.TAB)

        district = driver.find_element_by_id('CustomerData_AddressViewModel_District')
        district.send_keys(self.district + Keys.TAB)

        city = driver.find_element_by_id('CustomerData_AddressViewModel_City')
        city.send_keys(self.city + Keys.TAB)

        building = driver.find_element_by_id('CustomerData_AddressViewModel_BuildingName')
        building.send_keys(self.building + Keys.TAB)

        building_num = driver.find_element_by_id('CustomerData_AddressViewModel_StreetNumber')
        building_num.send_keys(self.building_num + Keys.TAB)

        street = driver.find_element_by_id('CustomerData_AddressViewModel_Street')
        street.send_keys(self.street + Keys.TAB)

        driver.implicitly_wait(200)
        driver.find_element_by_class_name('s4d-close-cookie').click()

        timeCombo = driver.find_element_by_id('SelectTime')
        timeCombo.click()

        times = Select(driver.find_element_by_id('SelectTime'))
        times.select_by_index(0)

        
        # payByCard = driver.find_element_by_class_name('s4d-payment-type')
        # payByCard.click()
        # driver.find_element_by_id('checkout-place-order').click()


    def inputCardDetails(self):
            driver = self.driver
            cardType = driver.find_element_by_name('paymentBrand')
            # cardType.click()

            brands = Select(driver.find_element_by_name('paymentBrand'))
            brands.select_by_index(1)


# def run(self):
#     print("in command loop")
#     # orderFood = FoodBot("Adam", "O Ceallaigh" , "0851152225" , "oceallaighadam96@gmail.com" , "Dublin 1" , "Dublin" , self.address , "Unit 1" , "N Wall Quay")
#     # orderFood.placeOrder()
#     # orderFood.inputDetails()

# wia.Command.subscribe(**{"device": deviceId, "slug": slug, "func": run})

# while True:
#     time.sleep(.1)

orderFood = FoodBot()
orderFood.placeOrder()
orderFood.inputDetails()