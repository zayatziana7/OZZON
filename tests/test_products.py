from locators.ozon_fresh_locators import OzonFreshPageLocators as Ozon
from locators.products_locators import OzonProductsLocatorss as Products


class TestProducts:
    def test_products(self, ozon_products):
        ozon_products.open_products()
        text = ozon_products.get_element_products_text(Ozon.OUR_PRODUCTS)
        assert text == "Наши продукты"


    def test_dairy(self, ozon_products):
        ozon_products.open_products()
        ozon_products.click_to_tabs_products(Products.DAIRY)
        text = ozon_products.get_element_products_text(Products.DAIRY_VALUE)
        assert text == "Молочные продукты и яйца Ozon fresh"


    def test_cheeses(self, ozon_products):
        ozon_products.open_products()
        ozon_products.click_to_tabs_products(Products.CHEESES)
        text = ozon_products.get_element_products_text(Products.CHEESES_VALUE)
        assert text == "Сыры Ozon fresh"


    def test_gastronomy(selfб, ozon_products):
        ozon_products.open_products()
        ozon_products.click_to_tabs_products(Products.GASTRONOMY)
        text = ozon_products.get_element_products_text(Products.GASTRONOMY_VALUE)
        assert text == "Гастрономия Ozon fresh"


    def test_grocery(selfб, ozon_products):
        ozon_products.open_products()
        ozon_products.click_to_tabs_products(Products.GROCERY)
        text = ozon_products.get_element_products_text(Products.GROCERY_VALUE)
        assert text == "Бакалея Ozon fresh"


    def test_sauces(selfб, ozon_products):
        ozon_products.open_products()
        ozon_products.click_to_tabs_products(Products.SAUCES)
        text = ozon_products.get_element_products_text(Products.SAUCES_VALUE)
        assert text == "Соусы, джемы и мёд Ozon fresh"


    def test_frozen_food(selfб, ozon_products):
        ozon_products.open_products()
        ozon_products.click_to_tabs_products(Products.FROZEN)
        text = ozon_products.get_element_products_text(Products.FROZEN_FOOD_PRODUCTS)
        assert text == "Замороженные продукты Ozon fresh"


    def test_sweets_and_snacks(self, ozon_products):
        ozon_products.open_products()
        ozon_products.click_to_tabs_products(Products.SWEETS_SNACKS)
        text = ozon_products.get_element_products_text(Products.SWEETS_SNACKS_VALUE)
        assert text == "Снеки и сладости Ozon fresh"


    def test_coffee_and_tea(selfб, ozon_products):
        ozon_products.open_products()
        ozon_products.click_to_tabs_products(Products.COFFEE_TEA)
        text = ozon_products.get_element_products_text(Products.COFFEE_TEA_VALUE)
        assert text == "Кофе и чай Ozon fresh"


    def test_beverages(selfб, ozon_products):
        ozon_products.open_products()
        ozon_products.click_to_tabs_products(Products.BEVERAGES)
        text = ozon_products.get_element_products_text(Products.BEVERAGES_VALUE)
        assert text == "Напитки Ozon fresh"


    def test_prepared_food(selfб, ozon_products):
        ozon_products.open_products()
        ozon_products.click_to_tabs_products(Products.PREPARED)
        text = ozon_products.get_element_products_text(Products.PREPARED_VALUE)
        assert text == "Готовая еда Ozon fresh"


    def test_our_barn(selfб, ozon_products):
        ozon_products.open_products()
        ozon_products.click_to_tabs_products(Products.OUR_BARN)
        text = ozon_products.get_element_products_text(Products.OUR_BARN_VALUE)
        assert text == "Пекарня Ozon fresh"


    def test_our_confectionery(selfб, ozon_products):
        ozon_products.open_products()
        ozon_products.click_to_tabs_products(Products.OUR_CONFECTIONERY)
        text = ozon_products.get_element_products_text(Products.OUR_CONFECTIONERY_VALUE)
        assert text == "Наша кондитерская"

