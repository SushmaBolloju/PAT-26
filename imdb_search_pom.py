import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IMDbSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, 'suggestion-search')
        self.dropdown = (By.XPATH, '//label[text()="Search by:"]/following-sibling::select')
        self.search_button = (By.XPATH, '//button[@id="suggestion-search-button"]')

    def fill_search_query(self, query):
        search_box = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.search_box))
        search_box.send_keys(query)

    def select_search_category(self, category):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.dropdown))
        dropdown.select_by_visible_text(category)

    def click_search_button(self):
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_button))
        search_button.click()

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_imdb_search(browser):
    # Open IMDb search page
    browser.get('https://www.imdb.com/search/name/')

    # Initialize IMDbSearchPage
    imdb_search_page = IMDbSearchPage(browser)

    # Fill search query
    imdb_search_page.fill_search_query('Tom Hanks')
 # Click search button
    imdb_search_page.click_search_button()

