import pytest

from locators.dairy_locators import OzonDairyLocators as Dairy



class TestDairy:

    @pytest.mark.parametrize('locator, locator_text, text_to_check', [
        (Dairy.VEGETABLE_EGGS, Dairy.VEGETABLE_EGGS_VALUE, "Яйца куриные Ozon fresh, С1, 10 шт"),
        (Dairy.CHICKEN_EGGS, Dairy.CHICKEN_EGGS_VALUE, "Яйца куриные Ozon fresh, С2, 10 шт"),
        (Dairy.SELECTED_EGGS, Dairy.SELECTED_EGGS_VALUE, "Яйца куриные Ozon fresh, отборные СО, 10 шт")

    ])
    def test_dairy_tab(self, ozon_dairy, locator, locator_text, text_to_check):
        ozon_dairy.test_open_dairy()
        ozon_dairy.click_to_tabs_dairy(locator)
        text = ozon_dairy.get_element_dairy_text(locator_text)
        assert text == text_to_check
