import pytest

from locators.ozon_fresh_locators import OzonFreshPageLocators as Fresh


class TestOzon:
    def test_recipes(self, ozon):
        ozon.open_ozon()
        text = ozon.get_element_ozonfresh_text(Fresh.VAIUE_RECIRES)
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
    def test_recipes_tab(self, ozon, locator, locator_text, text_to_check):
        ozon.open_ozon()
        ozon.click_to_tabs_ozonfresh(locator)
        text = ozon.get_element_ozonfresh_text(locator_text)
        assert text == text_to_check
