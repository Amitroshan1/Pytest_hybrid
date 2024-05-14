
from pageObject.LoginPage import Login
from utilities.readProperties import *
from utilities.customLogger import LogGen

from utilities import read_xl


class Test_002_DDT_login:
    baseUrl= ReadConfig.getAppUrl()
    path=".//TestData//testdata.xlsx"

    logger=LogGen.setup_logger()


    def test_login(self,setup):
        self.logger.info('*********************************Test_002_DDT_login********************')
        self.logger.info('*************************Verifing the login****************************')
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.lp=Login(self.driver)
        self.row = read_xl.Row_count(self.path,'Sheet1')
        self.col= read_xl.col_count(self.path,'Sheet1')

        lst_status=[]

        for r in range(2,self.row+1):

            self.username=read_xl.read_data(self.path,'Sheet1',r,1)
            self.password=read_xl.read_data(self.path,'Sheet1',r,2)
            self.exp_data=read_xl.read_data(self.path,'Sheet1',r,3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.loginButton()
            act_title=self.driver.title
            if act_title == "Dashboard / nopCommerce administration":
                if self.exp_data=="pass":
                    self.logger.info('****************************passed***********************')
                    lst_status.append('pass')
                    self.lp.Logout_click()
                elif self.exp_data=='fail':
                    self.logger.info('****************************failed***********************')
                    self.lp.Logout_click()
                    lst_status.append('fail')
            elif act_title != "Dashboard / nopCommerce administration":
                if self.exp_data=='pass':
                    self.logger.info('****************************failed***********************')
                    lst_status.append('fail')
                elif self.exp_data=='fail':
                    self.logger.info('****************************failed***********************')
                    lst_status.append('pass')

        if 'fail' not in lst_status:
            self.logger.info('****************************DDT PAssed***********************')
            self.driver.close()
            assert True
        else:
            self.logger.info('****************************DDT failed***********************')
            self.driver.close()
            assert False
        print(lst_status)




