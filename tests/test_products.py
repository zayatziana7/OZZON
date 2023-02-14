import pytest

from locators.ozon_fresh_locators import OzonFreshPageLocators as Ozon
from locators.products_locators import OzonProductsLocatorss as Products
from hamcrest import assert_that, equal_to, greater_than

class TestProducts:

    def test_products(self, ozon_products):
        ozon_products.open_products()
        text = ozon_products.get_element_products_text(Ozon.OUR_PRODUCTS)
        assert text == "Наши продукты"

    @pytest.mark.parametrize('locator, locator_text, text_to_check', [
        (Products.DAIRY, Products.DAIRY_VALUE, "Молочные продукты и яйца Ozon fresh"),
        (Products.CHEESES, Products.CHEESES_VALUE, "Сыры Ozon fresh"),
        (Products.GASTRONOMY, Products.GASTRONOMY_VALUE, "Гастрономия Ozon fresh"),
        (Products.GROCERY, Products.GROCERY_VALUE, "Бакалея Ozon fresh"),
        (Products.SAUCES, Products.SAUCES_VALUE, "Соусы, джемы и мёд Ozon fresh"),
        (Products.FROZEN, Products.FROZEN_FOOD_PRODUCTS, "Замороженные продукты Ozon fresh"),
        (Products.SWEETS_SNACKS, Products.SWEETS_SNACKS_VALUE, "Снеки и сладости Ozon fresh"),
        (Products.COFFEE_TEA, Products.COFFEE_TEA_VALUE, "Кофе и чай Ozon fresh"),
        (Products.BEVERAGES, Products.BEVERAGES_VALUE, "Напитки Ozon fresh"),
        (Products.PREPARED, Products.PREPARED_VALUE, "Готовая еда Ozon fresh"),
        (Products.OUR_BARN, Products.OUR_BARN_VALUE, "Пекарня Ozon fresh"),
        (Products.OUR_CONFECTIONERY, Products.OUR_CONFECTIONERY_VALUE, "Наша кондитерская")

    ])
    def test_products_tab(self, ozon_products, locator, locator_text, text_to_check):
        ozon_products.open_products()
        ozon_products.click_to_tabs_products(locator)
        text = ozon_products.get_element_products_text(locator_text)
        assert_that(text, equal_to(text_to_check), 'проверка не сошлась')
