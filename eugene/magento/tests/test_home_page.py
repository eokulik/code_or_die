import pytest
from pages.home_page import HomePage


def test_search_field(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.search_is_displayed()
    assert home_page.search_is_displayed()


@pytest.mark.parametrize('text', ['asdasd', 'qweqwe', 'zxczc'])
def test_search_works(driver, text):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.execute_search(text)
    assert home_page.check_url_is(f'https://magento.softwaretestingboard.com/catalogsearch/result/?q={text}')
