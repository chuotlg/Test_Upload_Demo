from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from pages.upload_page import Upload
from pages.base import BasePage


@given('I launch the chrome browser')
def launch_browser(self):
    self.driver = webdriver.Chrome()


@when('I open the \'upload file\' page')
def open_upload_page(self):
    self.driver.get(BasePage.upload_url)
    self.driver.maximize_window()
    wait = WebDriverWait(self.driver, BasePage.wait_time)


@when('I select a valid file to upload')
def select_file(self):
    Upload.upload_file(self, Upload.file_location)

@when('I accept the terms')
def click_terms(self):
    Upload.click_terms(self)

@when('I click on Submit btn')
def click_submit_btn(self):
    Upload.click_submit(self)

@then('a successful msg for uploading the file is displayed')
def check_successful_msg(self):
    Upload.verify_uploaded_msg(Upload.success_msg)

@then('close browser')
def close_browser(context):
    context.driver.close()

