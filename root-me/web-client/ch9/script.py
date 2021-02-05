import requests
from selenium import webdriver


# almost nothing to do, the password is shown in the Login() function in JS
url = 'http://challenge01.root-me.org/web-client/ch9/'

driver = webdriver.Chrome()

driver.get(url)

login_element = driver.find_element_by_name('pseudo')
login_element.send_keys('4dm1n')

pass_element = driver.find_element_by_name('password')
pass_element.send_keys('sh.org')

submit_btn = driver.find_element_by_name('button')
submit_btn.click()

print('answer should show')
