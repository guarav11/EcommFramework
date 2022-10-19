# it will read the common date from ini file

import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")   # in brackets path of config.ini file

class ReadConfig():
    @staticmethod       # so i can access below method just by using classname(ReadConfig) without creating object
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod  # so i can access below method just by using classname without creating object
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod  # so i can access below method just by using classname without creating object
    def getUserPassword():
        password = config.get('common info', 'password')
        return password