from selenium import webdriver
import time

url = 'http://challenge01.root-me.org/web-client/ch1/'

driver = webdriver.Chrome()

driver.get(url)

time.sleep(1)

alert = driver.switch_to.alert
time.sleep(1)
alert.send_keys('123456azerty')
alert.accept()

print('Response should be accepted')
