from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

class AddCustomer:
    lnkCustomerMenu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomermenulist_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddNew_xpath="//a[@class='btn btn-primary']"
    txtEmail_id='Email'
    txtPassword_id='Password'
    txtFirstName_id='FirstName'
    txtLastName_id='LastName'
    rdoMale_id='Gender_Male'
    rdoFemale_id='Gender_Female'
    calender_id='DateOfBirth'
    txtComapny_id='Company'
    chkBoxTaxExempt_xpath="//input[@id='Company' and @name='IsTaxExempt']"

    txtNewsletter_xpath="(//input[@class='select2-search__field'])[1]"
    News_option_1_id="//li[@class='select2-results__option select2-results__option--highlighted'  and text()='Test store 2']"
    newsSelect_xp="//select[@id='SelectedNewsletterSubscriptionStoreIds']"


    txtCusmtomerRole_xpath="(//input[@class='select2-search__field'])[2]"
    selectCustRole_id='SelectedCustomerRoleIds'
    cancle_xpath="(//span[@class='select2-selection__choice__remove'])[2]"


    drpdwn_xpath="//select[@class='form-control valid']"
    chkbox_active="//input[@id='Active']"
    txtAreaAdmin_id='AdminComment'
    btnSave_xpath="(//button[@class='btn btn-primary'])[1]"

    sucessfull_msg_xp="//div[@class='alert alert-success alert-dismissable']"

    def __init__(self,driver):
        self.driver=driver


    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomerMenu_xpath).click()
        sleep(1)

    def clickOnCustomerList(self):
        self.driver.find_element(By.XPATH,self.lnkCustomermenulist_xpath).click()
        sleep(1)

    def clickOnAddButton(self):
        self.driver.find_element(By.XPATH,self.btnAddNew_xpath).click()
        sleep(1)

    def enterEmailid(self,email):
        self.driver.find_element(By.ID,self.txtEmail_id).send_keys(email)

    def enterPassword(self,password):
        self.driver.find_element(By.ID,self.txtPassword_id).send_keys(password)

    def enterFirstname(self,first):
        self.driver.find_element(By.ID,self.txtFirstName_id).send_keys(first)


    def enterLastName(self,last):
        self.driver.find_element(By.ID,self.txtLastName_id).send_keys(last)

    def genderRadio(self,gender):
        if gender == 'Male':
            self.driver.find_element(By.ID,self.rdoMale_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID,self.rdoFemale_id).click()
        else:
            self.driver.find_element(By.ID, self.rdoMale_id).click()


    def dateOfBirth(self,date):
        self.driver.find_element(By.ID,self.calender_id).send_keys(date)

    def enterCompanyName(self,Com_Name):
        self.driver.find_element(By.ID,self.txtComapny_id).send_keys(Com_Name)

    def isTaxExempt(self):
        self.driver.find_element(By.XPATH,self.chkBoxTaxExempt_xpath).click()

    def news_option(self,option):
        self.driver.find_element(By.XPATH,self.txtNewsletter_xpath).click()
        sleep(2)
        opt=Select(self.driver.find_element(By.XPATH,self.newsSelect_xp))
        if option == 'Test store 2':
            opt.select_by_visible_text("Test store 2")
        else:
           opt.select_by_visible_text("Your store name")
        sleep(1)
        self.driver.find_element(By.XPATH, self.txtNewsletter_xpath).click()
        sleep(2)


    def customer_Role(self,role):
        self.driver.find_element(By.XPATH,self.txtCusmtomerRole_xpath).click()
        sleep(2)
        opt=Select(self.driver.find_element(By.ID,self.selectCustRole_id))
        if role == 'Administrators':
            self.listitem=opt.select_by_visible_text('Administrators')
        elif role == 'Forum Moderators':
            self.listitem=opt.select_by_visible_text('Forum Moderators')
        elif role == 'Registered':
            self.listitem=opt.select_by_visible_text('Registered')
        elif role == 'Guests':
            self.driver.find_element(By.XPATH, self.txtCusmtomerRole_xpath).click()
            sleep(2)

            self.driver.find_element(By.XPATH,self.cancle_xpath).click()
            self.listitem =opt.select_by_visible_text('Guests')
        elif role == 'Vendors':
            self.listitem = opt.select_by_visible_text('Vendors')
        else:
            print("into else block")
            self.driver.find_element(By.XPATH, self.txtCusmtomerRole_xpath).click()
            sleep(2)
            self.driver.find_element(By.XPATH, self.cancle_xpath).click()
            self.listitem =opt.select_by_visible_text('Guests')
            sleep(4)
        self.driver.find_element(By.XPATH, self.txtCusmtomerRole_xpath).click()
        sleep(2)


    def setManagerOfVender(self,manager):
        dropdwn=Select(self.driver.find_element(By.ID,'VendorId'))
        dropdwn.select_by_visible_text(manager)

    def setAdminContent(self,content):
        self.driver.find_element(By.ID,self.txtAreaAdmin_id).send_keys(content)
        sleep(1)
    def saveButton(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()




