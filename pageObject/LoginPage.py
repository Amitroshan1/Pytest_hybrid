from selenium.webdriver.common.by import By


class Login:
    textbox_username_xpath = "//input[@name='Email']"
    textbox_password_xpath = "//input[@name='Password']"
    button_Login_xpath = "//button[@type='submit']"
    logout_button_xpath= "//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    # action Methods
    def setUserName(self, UserName):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(UserName)

    def setPassword(self, Password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(Password)

    def loginButton(self):
        self.driver.find_element(By.XPATH, self.button_Login_xpath).click()

    def Logout_click(self):
        self.driver.find_element(By.XPATH,self.logout_button_xpath).click()



