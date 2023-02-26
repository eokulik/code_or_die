from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
driver.get('https://www.google.com/')
sleep(3)
driver.maximize_window()
print(driver.current_url)
print(driver.title)
search_field = driver.find_element(By.NAME, 'q')
print(search_field.tag_name)
print(search_field.get_attribute('title'))
print(search_field.value_of_css_property('height'))
search_field.click()
search_field.clear()
search_field.send_keys('cat')
search_field.submit()
sleep(5)
