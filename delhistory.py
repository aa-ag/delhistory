###--- DELETE BROWSER HISTORY ---###
import os
from selenium import webdriver
import sqlite3

#--- Delete from database with Python ---#

def clear_cache(browser):
    '''
    Clear cookies and cache from ChromeDriver instance.
    '''
    try:
        browser.get('chrome//settings/clearBrowserData')
        browser.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)

    except Exception as x:
        print(str(x))
        browser.quit()

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
clear_cache(browser)

#--- Delete from database in machine with Python ---#
# conn = sqlite3.connect("/Users/aaronaguerrevere/Library/Safari/History.db")

# cursor = conn.cursor()

# id = 0

# result = True

# while result:
#     ids = list()

#     for row in cursor.execute("SELECT * FROM urls"):
#         print(row)

#         id = row[0]
#         ids.append((id,))

#     cursor.executemany('DELETE * FROM urls WHERE id = ?', ids)

#     conn.commit()

# conn.close()