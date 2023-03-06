from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    return chrome_driver


def test_hover(driver):
    driver.get('https://demoqa.com/menu')
    sleep(5)
    main_item2 = driver.find_element(By.LINK_TEXT, 'Main Item 2')
    actions = ActionChains(driver)
    # ActionChains(driver).move_to_element(main_item2).click(sub_item).perform()
    actions.move_to_element(main_item2)
    actions.pause(1)
    sub_item = driver.find_element(By.LINK_TEXT, 'SUB SUB LIST »')
    actions.move_to_element(sub_item)
    actions.pause(3)
    actions.perform()


def test_hover_magento(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    women = driver.find_element(By.ID, 'ui-id-4')
    actions = ActionChains(driver)
    actions.move_to_element(women)
    tops = driver.find_element(By.ID, 'ui-id-9')
    actions.click(tops)
    actions.perform()


def test_new_tab(driver):
    driver.get('https://www.qa-practice.com/elements/new_tab/link')
    link = driver.find_element(By.ID, 'new-page-link')
    link.click()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == 'I am a new page in a new tab'
    driver.close()
    driver.switch_to.window(tabs[0])


def test_iframe(driver):
    driver.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    driver.find_element(By.LINK_TEXT, 'Iframe').click()
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    button = driver.find_element(By.CLASS_NAME, 'btn-primary')
    print(button.text)
    driver.switch_to.default_content()
    driver.find_element(By.LINK_TEXT, 'Iframe').click()


def test_drag_n_drop(driver):
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    draggable = driver.find_element(By.ID, 'rect-draggable')
    droppable = driver.find_element(By.ID, 'rect-droppable')
    # ActionChains(driver).move_to_element(draggable).click_and_hold(draggable).move_to_element(droppable).release(droppable).perform()
    ActionChains(driver).drag_and_drop(draggable, droppable).perform()
    sleep(3)
    ActionChains(driver).double_click()
    ActionChains(driver).context_click()
    ActionChains(driver).key_down(Keys.CONTROL).click(droppable).key_up(Keys.CONTROL).perform()  # control+click

    assert 'Dropped!' in droppable.text
