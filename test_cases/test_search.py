import pytest
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from page_objects.HomePage import HomePage


@pytest.fixture
def driver():
    _driver = webdriver.Chrome(ChromeDriverManager().install())
    _driver.get("https://www.amazon.com.mx")
    _driver.implicitly_wait(20)

    yield _driver

    _driver.quit()


def test_search_text_box(driver):
    home_page = HomePage(driver)
    home_page.search_text_box.send_keys("Videojuegos")
    home_page.search_button.click()

    time.sleep(20)

    assert "Videojuegos" in driver.current_url
    assert "Videojuegos" in driver.title