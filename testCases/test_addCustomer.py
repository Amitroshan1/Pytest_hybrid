import random
import string
from time import sleep

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObject.LoginPage import Login
from pageObject.AddCustomer import AddCustomer
from selenium.webdriver.common.by import By



class Test_AddCustomer:
    base_URL=ReadConfig.getAppUrl()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()

    logger=LogGen().setup_logger()



    def test_003_addCustomer(self,setup):
        self.driver=setup
        self.loginpage = Login(setup)
        self.logger.info('******************test_003_addCustomer************************')
        self.logger.info('*********************** adding new customer ******************')
        self.driver.get(self.base_URL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        self.loginpage.setUserName(self.username)
        self.loginpage.setPassword(self.password)
        self.loginpage.loginButton()
        self.logger.info('*************************** login successfull*******************')

        self.addCust=AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOnCustomerList()
        self.addCust.clickOnAddButton()
        self.logger.info('********************** entering the details ********************')

        self.email=stringGenerator() + '@gmail.com'
        self.addCust.enterEmailid(self.email)
        self.addCust.enterPassword('test123')
        self.addCust.enterFirstname('amit')
        self.addCust.enterLastName('kumar')
        self.addCust.genderRadio('Male')
        self.logger.info('***************************** Date of Birth *********************')
        self.addCust.dateOfBirth('02/10/1998')
        self.addCust.enterCompanyName('tchtwister')
        self.driver.execute_script('scrollBy(0,300)')

        self.addCust.news_option('ndjbcb')
        self.logger.info('*********************** clicked on news letter **********************')
        self.addCust.customer_Role('Registered')
        self.addCust.setManagerOfVender('Vendor 2')
        self.addCust.setAdminContent("hi this is just a test")
        self.save=self.driver.find_element(By.XPATH,self.addCust.btnSave_xpath)
        self.driver.execute_script('arguments[0].scrollIntoView(true)',self.save)
        self.addCust.saveButton()
        self.sucess=self.driver.find_element(By.XPATH,self.addCust.sucessfull_msg_xp)
        if self.sucess.is_displayed():
            assert True
        else:
            self.driver.save_screenshot('.\\ScreeShot\\addcustomer.png')
            assert False

        sleep(15)




def stringGenerator(size=8,char=string.ascii_lowercase + string.digits):
    return "".join(random.choice(char) for _ in range(size))



