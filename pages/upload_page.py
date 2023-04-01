from selenium.webdriver.common.by import By
from pages.base import BasePage


class Upload(BasePage):
    # define the locators of all elements using for this page here
    submit_file_btn = (By.ID, 'submitbutton')
    choose_file_btn = (By.NAME, 'uploadfile_0')
    terms_chkbox = (By.NAME, 'uploadfile_0')
    file_location = "E: / Test / java.js"
    upload_msg = (By.XPATH, '//*[@id="res"]/center')
    success_msg = "1 file has been successfully uploaded."

    def __init__(self, driver):
        self.driver = driver

    def upload_file(self, string):
        file_btn = self.driver.find_element(self.choose_file_btn)
        file_btn.send_keys(self.file_location)

    def click_terms(self):
        file_btn = self.driver.find_element(self.terms_chkbox)
        file_btn.click()

    def click_submit(self):
        submit_btn = self.driver.find_element(self.submit_file_btn)
        submit_btn.click()

    def verify_uploaded_msg(self):
        exist = self.driver.find_element(self.upload_msg).get_attribute("textContent")
        # print(self.driver.find_element(By.XPATH, '//*[@id="res"]/center/text()[1]').is_displayed())
        if exist == self.success_msg:
            assert True, "Successful msg for uploading file is displayed"
        else:
            assert False, "No successful msg for uploading is displayed"
