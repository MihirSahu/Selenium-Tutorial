from selenium import webdriver


class Booking(webdriver.Chrome):
    #This is the constructor
    def __init__(self, driver_path='~/CLI_programs/chromedriver'):
        self.driver_path = driver_path
