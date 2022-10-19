import random
import string

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddCustomer import AddCustomer
from selenium.webdriver.common.by import By


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()  # using classname we directly called methods from ReadConfig because they are static methods in under ReadConfig Class
    username = ReadConfig.getUsername()
    password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()   # it will return logger method and i am saving it in a variable called logger

    @pytest.mark.sanity
    def test_addcustomer(self, setup):
        self.logger.info("***** Test_003_AddCustomer *****")
        self.logger.info("***** Login process starts *****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("***** Login Successful *****")

        self.logger.info("***** Add Customer Starts *****")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMainMenu()
        self.addcust.clickOnCustomerMenuitems()
        self.addcust.clickOnAddnew()

        self.logger.info("***** Providing customer details *****")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test122")
        self.addcust.setFirstName("Gaurav")
        self.addcust.setLastName("Singh")
        self.addcust.genderSelection("Male")
        self.addcust.dob("12/12/2010")
        self.addcust.selectCompanyName("Voiceoc")
        self.addcust.taxSelection()
        self.addcust.isActive()
        self.addcust.customerRoles()
        self.addcust.registered()
        self.addcust.saveDetails()

        self.logger.info("***** saving customer details *****")

        self.logger.info("***** Validation starts *****")

        self.msg = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']").text

        print(self.msg)
        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("***** Add customer Test passed *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("***** Add customer Test failed *****")
            assert True == False

        self.driver.close()
        self.logger.info("***** Ending  *****")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))






