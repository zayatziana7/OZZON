from locators.dairy_locators import OzonDairyLocators as Dairy



class TestDairy:


    def test_vegetable_eggs(self, ozon_dairy):
        ozon_dairy.test_open_dairy()
        ozon_dairy.click_to_tabs_dairy(Dairy.VEGETABLE_EGGS)
        text = ozon_dairy.get_element_dairy_text(Dairy.VEGETABLE_EGGS_VALUE)
        assert text == "Яйца куриные Ozon fresh, С1, 10 шт"


    def test_chicken_eggs(self, ozon_dairy):
        ozon_dairy.test_open_dairy()
        ozon_dairy.click_to_tabs_dairy(Dairy.CHICKEN_EGGS)
        text = ozon_dairy.get_element_dairy_text(Dairy.CHICKEN_EGGS_VALUE)
        assert text == "Яйца куриные Ozon fresh, С2, 10 шт"


    def test_selected_eggs(self, ozon_dairy):
        ozon_dairy.test_open_dairy()
        ozon_dairy.click_to_tabs_dairy(Dairy.SELECTED_EGGS)
        text = ozon_dairy.get_element_dairy_text(Dairy.SELECTED_EGGS_VALUE)
        assert text == "Яйца куриные Ozon fresh, отборные СО, 10 шт"
