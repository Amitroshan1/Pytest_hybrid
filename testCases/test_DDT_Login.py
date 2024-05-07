import pytest
from selenium import webdriver
from pageObject.LoginPage import Login
from utilities.readProperties import *
from utilities.customLogger import LogGen
from time import sleep


class Test_001_login:
    baseUrl= ReadConfig.getAppUrl()
    username= ReadConfig.getUsername()
    password= ReadConfig.getPassword()

    logger=LogGen.setup_logger()



    def test_homepage_title(self,setup):
        self.logger.info('****************************Test_001_Login*************************')
        self.logger.info('****************************Verifing Home Page Title**************')
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        act_title=self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info('************************Home Page Title is passed***************')
        else:
            self.driver.save_screenshot(".\\ScreenShot\\test_homePageTitle.png")
            self.driver.close()
            self.logger.info('************************Home Page Title is passed***************')
            assert False

    def test_login(self,setup):
        self.logger.info('*************************Test_001_Login*******************************')
        self.logger.info('*************************Verifing the login****************************')
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.loginButton()
        act_title=self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info('****************************LOgin Is sussesfull***********************')
            self.driver.close()
        else:
            self.driver.save_screenshot('.\\ScreenShot\\log')
            self.logger.info('****************************LOgin Is Failed***********************')
            self.driver.close()
            assert False
