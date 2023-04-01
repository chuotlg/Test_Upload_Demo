from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


# This is place to define all common items for other page to re-use
class BasePage():
    upload_url = "https://demo.guru99.com/test/upload/"
    wait_time = 5

    def __init__(self, driver):
        self.driver = driver
