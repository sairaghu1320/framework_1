""" Contains the configurations required by the project"""


class Config:
    CHROMEDRIVER_PATH = "../drivers1/chromedriver.exe"
    GECKODRIVER_PATH = "../drivers1/geckodriver.exe"
    EDGEDRIVER_PATH = "../drivers1/msedgedriver.exe"
    LOCATORS_FILE_PATH = r"../files/Actitime_Locators.xlsx"
    LOGIN_SHEET_NAME = "LoginPageObjects"
    URL = "https://demo.actitime.com/login.do"
    BROWSER_NAME = "safari"
