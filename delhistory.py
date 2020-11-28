###--- DELETE BROWSER HISTORY ---###
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

#--- Delete from database with Python ---#

def get_button(driver):
    return driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')

def clear_cache(driver, timeout=60):
    driver.get('brave://settings/clearBrowserData')
    options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'

    wait = WebDriverWait(driver, timeout)
    wait.until(get_button)

    get_button(driver).click()

    wait.until_not(get_button)

driver_path = '/usr/local/bin/chromedriver'
options = Options()
driver = webdriver.Chrome(options = options, executable_path = driver_path)
clear_cache(driver)