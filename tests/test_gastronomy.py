from locators.gastronomy_locators import OzonGastronomysLocators as Gastronomy
from locators.products_locators import OzonProductsLocatorss


class TestGastronomy:



    def test_healthy_lifestyle_fresh(self, ozon_gastronomy):
        ozon_gastronomy.open_gastronomy()
        ozon_gastronomy.click_to_tabs_gastronomy(Gastronomy.HEALTHY_LIFESTYLE_FRESH)
        text = ozon_gastronomy.get_element_gastronomy_text(Gastronomy.HEALTHY_LIFESTYLE_FRESH_VALUE)
        assert text == "Хумус Ozon fresh, со свеклой, 160 г"

    def test_meat_poultry_and_fish(self, ozon_gastronomy):
        ozon_gastronomy.open_gastronomy()
        ozon_gastronomy.click_to_tabs_gastronomy(Gastronomy.MEAT_POUITRY_FISH)
        text = ozon_gastronomy.get_element_gastronomy_text(Gastronomy.MEAT_POUITRY_FISH_VALUE)
        assert text == "Колбасы и деликатесы"

    def test_prepared_food(self, ozon_gastronomy):
        ozon_gastronomy.open_gastronomy()
        ozon_gastronomy.click_to_tabs_gastronomy(Gastronomy.PREPARED_FOOD)
        text = ozon_gastronomy.get_element_gastronomy_text(Gastronomy.PREPARED_FOOD_VALUE)
        assert text == "Салаты и закуски"

    def test_frozen_food(self, ozon_gastronomy):
        ozon_gastronomy.open_gastronomy()
        ozon_gastronomy.click_to_tabs_gastronomy(Gastronomy.FROZEN_FOOD)
        text = ozon_gastronomy.get_element_gastronomy_text(Gastronomy.FROZEN_FOOD_VALUE)
        assert text == "Полуфабрикаты"

    def test_grocery_canned_food(self, ozon_gastronomy):
        ozon_gastronomy.open_gastronomy()
        ozon_gastronomy.click_to_tabs_gastronomy(Gastronomy.GROCERY)
        text = ozon_gastronomy.get_element_gastronomy_text(Gastronomy.GROCERY_VALUE)
        assert text == "Консервы"

    def test_grocery_butter_sauces_ketchups(self, ozon_gastronomy):
        ozon_gastronomy.open_gastronomy()
        ozon_gastronomy.click_to_tabs_gastronomy(Gastronomy.GROCERY_G)
        text = ozon_gastronomy.get_element_gastronomy_text(Gastronomy.BATTER_SAUCES_KETCHUPS_VALUE)
        assert text == "Масло, соусы, кетчупы"
