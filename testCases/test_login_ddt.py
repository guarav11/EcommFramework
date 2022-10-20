import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()  # using classname we directly called methods from ReadConfig because they are static methods in under ReadConfig Class
    path = ".//TestData/LoginData.xlsx"

    logger = LogGen.loggen()   # it will return logger method and i am saving it in a variable called logger

    def test_login(self,setup):
        self.logger.info("***** Test_002_DDT_Login *****")
        self.logger.info("***** Verifying Login functionality *****")

        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)   # we have passed self.driver here because constructor in Login Class need this driver parameter And when I have created object of the Login class constructor automatically invokes

        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows i in Excel:", self.rows)

        list_status = []

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title


            if act_title=="Dashboard / nopCommerce administration":
                if self.exp=="Pass":
                    list_status.append("Pass")
                    self.logger.info("***** Passed ******")
                    self.lp.clickLogout()

                elif self.exp=="Fail":
                    list_status.append("Fail")
                    self.logger.info("***** Failed ******")
                    self.lp.clickLogout()


            elif act_title!="Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    list_status.append("Fail")
                    self.logger.info("***** Failed ******")


                elif self.exp == "Fail":
                    list_status.append("Pass")
                    self.logger.info("***** Passed ******")



        if "Fail" in list_status:
            self.logger.info("*****Test_002_DDT_Login Failed ******")
            self.driver.close()
            assert False
        else:
            self.logger.info("*****Test_002_DDT_Login Passed ******")
            self.driver.close()
            assert True


        self.logger.info("***** Test_002_DDT_Login  finished *****")