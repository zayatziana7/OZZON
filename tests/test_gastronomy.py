import pytest

from locators.gastronomy_locators import OzonGastronomysLocators as Gastronomy
from hamcrest import assert_that, equal_to, greater_than


class TestGastronomy:

    @pytest.mark.parametrize('locator, locator_text, text_to_check', [
        (Gastronomy.HEALTHY_LIFESTYLE_FRESH, Gastronomy.HEALTHY_LIFESTYLE_FRESH_VALUE, "Хумус Ozon fresh, со свеклой, 160 г"),
        (Gastronomy.MEAT_POUITRY_FISH, Gastronomy.MEAT_POUITRY_FISH_VALUE, "Колбасы и деликатесы"),
        (Gastronomy.PREPARED_FOOD, Gastronomy.PREPARED_FOOD_VALUE, "Салаты и закуски"),
        (Gastronomy.FROZEN_FOOD, Gastronomy.FROZEN_FOOD_VALUE, "Полуфабрикаты"),
        (Gastronomy.GROCERY, Gastronomy.GROCERY_VALUE, "Консервы"),
        (Gastronomy.GROCERY_G, Gastronomy.BATTER_SAUCES_KETCHUPS_VALUE, "Масло, соусы, кетчупы")

    ])
    def test_gastronomy_tab(self, ozon_gastronomy, locator, locator_text, text_to_check):
        ozon_gastronomy.open_gastronomy()
        ozon_gastronomy.click_to_tabs_gastronomy(locator)
        text = ozon_gastronomy.get_element_gastronomy_text(locator_text)
        assert_that(text, equal_to(text_to_check), 'проверка не сошлась')
