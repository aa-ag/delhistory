###--- DELETE BROWSER HISTORY ---###
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#--- Delete from database with Python ---#

def get_button(driver):
    return driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')

def clear_cache(driver, timeout=60):
    driver.get('chrome://settings/clearBrowserData')

    wait = WebDriverWait(driver, timeout)
    wait.until(get_button)

    get_button(driver).click()

    wait.until_not(get_button)

driver = webdriver.Chrome()
clear_cache(driver)