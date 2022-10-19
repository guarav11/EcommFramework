import random
import string
import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
from pageObjects.SearchCustomer import SearchCustomer
from pageObjects.AddCustomer import AddCustomer


class Test_004_SearchCustomer:
    baseURL = ReadConfig.getApplicationURL()  # using classname we directly called methods from ReadConfig because they are static methods in under ReadConfig Class
    username = ReadConfig.getUsername()
    password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()   # it will return logger method and i am saving it in a variable called logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_searchcustomer(self, setup):
        self.logger.info("***** Test_004_AddCustomer *****")
        self.logger.info("***** Login process starts *****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("***** Login Successful *****")

        addcustomer = AddCustomer(self.driver)
        addcustomer.clickOnCustomerMainMenu()
        time.sleep(8)
        addcustomer.clickOnCustomerMenuitems()
        time.sleep(4)


        scustomer = SearchCustomer(self.driver)
        scustomer.setEmail("victoria_victoria@nopCommerce.com")
        scustomer.clicksearch()
        time.sleep(5)

        status = scustomer.searchCustomerByEMail("victoria_victoria@nopCommerce.com")
        assert True==status
        self.logger.info("***** Test_004_SearchCustomer finished *****")










