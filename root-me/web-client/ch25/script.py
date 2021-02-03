import requests
from selenium import webdriver


# basic web-scrapping script, we remove disabled attributes in tags, and make the request
url = 'http://challenge01.root-me.org/web-client/ch25/'

driver = webdriver.Chrome()

javascript = "elements = document.getElementsByTagName('input'); elements[0].removeAttribute('disabled'); elements[1].removeAttribute('disabled');"
driver.get(url)
driver.execute_script(javascript)

user_input = driver.find_element_by_name('auth-login')
user_input.send_keys('hello')

submit_btn = driver.find_element_by_name('authbutton')
submit_btn.click()

response = driver.find_element_by_class_name('success')

print('answer: ' + response.text)

driver.close()
