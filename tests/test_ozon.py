import pytest

from locators.ozon_fresh_locators import OzonFreshPageLocators as Fresh
from hamcrest import assert_that, equal_to, greater_than

class TestOzon():
    def test_recipes(self, ozon_recipes_page):
        text = ozon_recipes_page.get_element_text(Fresh.VAIUE_RECIRES)
        assert text == "Рецепты"

    @pytest.mark.parametrize('locator, locator_text, text_to_check', [
        (Fresh.BREAKFASTS, Fresh.BREAKFASTS, "Завтраки"),
        (Fresh.FIRST_MEAL, Fresh.FIRST_MEAL, "Первые блюда"),
        (Fresh.SECOND_DISHES, Fresh.SECOND_DISHES, "Вторые блюда"),
        (Fresh.SALADS, Fresh.SALADS, "Салаты"),
        (Fresh.CNACKS, Fresh.CNACKS, "Закуски"),
        (Fresh.DESSERTS, Fresh.DESSERTS, "Десерты"),
        (Fresh.COUNTRIES, Fresh.COUNTRIES, "Из разных стран"),


    ])
    def test_recipes_tab(self, ozon_recipes_page, locator, locator_text, text_to_check):
        ozon_recipes_page.open_ozon()
        ozon_recipes_page.open_ozonfresh_tab(locator)
        text = ozon_recipes_page.get_element_text(locator_text)
        assert_that(text, equal_to(text_to_check), 'проверка не сошлась')
