import time
from selenium.webdriver.common.by import By

class AddCustomer:
    # Add Customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstname_xpath = "//input[@id='FirstName']"
    txtLastname_xpath = "//input[@id='LastName']"
    rdMaleGender_xpath = "//input[@id='Gender_Male']"
    rdFemaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    chkboxTax_xpath = "//input[@id='IsTaxExempt']"
    chkboxActive_xpath = "//input[@id='Active']"
    txtCustomerRoles_xpath = "(//div[@role='listbox'])[2]"
    lstitemRegistered_xpath = "//span[normalize-space()='Registered']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomerMainMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuitems(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH, self.txtFirstname_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.XPATH, self.txtLastname_xpath).send_keys(lastname)

    def genderSelection(self,gender):
        if gender=="Male":
            self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdFemaleGender_id).click()


    def dob(self,dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def selectCompanyName(self,company):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(company)

    def taxSelection(self):
        self.driver.find_element(By.XPATH, self.chkboxTax_xpath).click()

    def isActive(self):
        self.driver.find_element(By.XPATH, self.chkboxActive_xpath).click()

    def customerRoles(self):
        self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()

    def registered(self):
        self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath).click()

    def saveDetails(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()







