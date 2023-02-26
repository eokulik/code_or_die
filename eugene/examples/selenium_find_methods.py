from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get('https://www.qa-practice.com/')
sleep(3)
driver.maximize_window()
hello = driver.find_element(By.TAG_NAME, 'h1')
print(hello.text)
text_input_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Text input')
text_input_link.click()
expand_button = driver.find_element(By.CLASS_NAME, 'bi-caret-down')
expand_button.click()
text_string = driver.find_element(By.ID, 'id_text_string')
text_string.send_keys('Code or Die')
text_string.submit()
# email_field_tab = driver.find_element(By.XPATH, '//a[@href="/elements/input/email"]')
email_field_tab = driver.find_element(By.CSS_SELECTOR, 'a[href="/elements/input/email"]')
email_field_tab.click()

sleep(5)

