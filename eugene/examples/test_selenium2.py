from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    return chrome_driver


def test_click_simple_button(driver):
    driver.get('https://www.qa-practice.com/elements/button/simple')
    button = driver.find_element(By.ID, 'submit-id-submit')
    button.click()
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == 'Submitted'


def test_click_like_a_button(driver):
    driver.get('https://www.qa-practice.com/elements/button/like_a_button')
    button = driver.find_element(By.LINK_TEXT, 'Click')
    button.click()
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == 'Submitted'


def test_simple_button_enabled(driver):
    driver.get('https://www.qa-practice.com/elements/button/simple')
    button = driver.find_element(By.ID, 'submit-id-submit')
    assert button.is_displayed()
    assert button.is_enabled()


def test_select(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select_input = driver.find_element(By.ID, 'id_choose_language')
    select = Select(select_input)
    select.select_by_index(3)
    button = driver.find_element(By.ID, 'submit-id-submit')
    button.click()
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == 'JavaScript'


def test_click_third_tab(driver):
    sleep(3)
    driver.get('https://www.qa-practice.com/elements/input/simple')
    tabs = driver.find_elements(By.CLASS_NAME, 'tab')
    # third_tab = tabs[2]
    # third_tab.click()
    tabs[2].click()
    sleep(3)


def test_find_inside_an_element(driver):
    sleep(3)
    driver.get('https://www.qa-practice.com/elements/popup/modal')
    button = driver.find_element(By.CLASS_NAME, 'btn-primary')
    button.click()
    # sleep(2)
    pop_up = driver.find_element(By.CLASS_NAME, 'modal-content')
    send_button = pop_up.find_element(By.CLASS_NAME, 'btn-primary')
    send_button.click()
    sleep(3)


def test_magento(driver):
    sleep(3)
    driver.get('https://demoqa.com/dynamic-properties')
    button = driver.find_element(By.ID, 'enableAfter')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button))
    assert button.is_enabled()
    sleep(3)
