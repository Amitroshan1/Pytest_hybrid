import configparser

config=configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')

# for every variable we need to create static method
# we can acess static method without creating object for the class

class ReadConfig():

    @staticmethod
    def getAppUrl():
        url=config.get('common info','base_url')
        return url


    @staticmethod
    def getUsername():
        username=config.get('common info','username')
        return username


    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password