from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


class BasePage():
    upload_url = "https://demo.guru99.com/test/upload/"
    wait_time = 5

    def __init__(self, driver):
        self.driver = driver
