from selenium.webdriver.common.by import By
from utilities import XLUtils
from utilities.XLUtils import readData


class SearchCustomer:
    # Add customer page
    # txt_Email_id = "SearchEmail"
    file = "C:\\Users\\Gaurav\\PycharmProjects\\EcommFramework\\TestData\\Xpath.xlsx"
    sheetname = "SearchC"
    txt_Email_id = readData(file,sheetname,2,2)
    txt_FirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"

    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txt_Email_id).clear()
        self.driver.find_element(By.ID, self.txt_Email_id).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.txt_FirstName_id).clear()
        self.driver.find_element(By.ID, self.txt_FirstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lname)

    def clicksearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def getNoofRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoofColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))

    def searchCustomerByEMail(self, email):
        flag = False
        for r in range(1, self.getNoofRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if email==emailid:
                flag = True
                break

        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoofRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[3]").text
            if name==Name:
                flag = True
                break

        return flag









