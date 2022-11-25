# всегда должен быть этот файл для текстер пайтеста. лежат функции
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import constants
from mane_page.cheeses_page import OzonCheesesPage
from mane_page.dairy_page import OzonDairyPage
from mane_page.gastronomy_page import OzonGastronomyPage
from mane_page.house_garden_page import OzonHouseGardenPage
from mane_page.mothers_children_page import OzonMothersСhildrenPage
from mane_page.ozon_fresh_page import OzonPages
from mane_page.products_page import OzonProductsPage
from mane_page.sezon_page import OzonSezonPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()




@pytest.fixture()
def ozon_gastronomy(driver):
    return OzonGastronomyPage(driver)

@pytest.fixture()
def ozon_cheeses(driver):
    return OzonCheesesPage(driver)

@pytest.fixture()
def ozon_dairy(driver):
    return OzonDairyPage(driver)

@pytest.fixture()
def ozon_house_garden(driver):
    return OzonHouseGardenPage(driver)

@pytest.fixture()
def ozon_products(driver):
    return OzonProductsPage(driver)


@pytest.fixture()
def ozon_mothers_children(driver):
    return OzonMothersСhildrenPage(driver)

@pytest.fixture()
def ozon(driver):
    return OzonPages(driver)

@pytest.fixture()
def ozon_sezon(driver):
    return OzonSezonPage(driver)




@pytest.fixture(autouse=True, scope='function')
def open_ozon_url(driver):
    """
    autouse=True ---открывает автоматически
    scope='function'--- на каком уровне использовать для каждого теста
    :param driver:
    :return:
    """
    driver.get(constants.APP_URL)
