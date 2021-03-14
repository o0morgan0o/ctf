from selenium import webdriver
import time

from selenium.webdriver.common import alert

# passwrod is almost hardcoded in javascript, so very easy to extract

url = 'http://challenge01.root-me.org/web-client/ch11/'

driver = webdriver.Chrome()

driver.get(url)

login_btn = driver.find_element_by_tag_name('input')
login_btn.click()

alert1 = driver.switch_to.alert
time.sleep(1)
alert1.send_keys('GOD')
alert1.accept()

alert2 = driver.switch_to.alert
time.sleep(1)
alert2.send_keys('HIDDEN')
alert2.accept()

alert_response = driver.switch_to.alert


print(alert_response.text)
