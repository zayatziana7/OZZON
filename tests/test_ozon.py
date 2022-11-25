from locators.ozon_fresh_locators import OzonFreshPageLocators as Fresh


class TestOzon:
    def test_recipes(self,ozon):
        ozon.open_ozon()
        text = ozon.get_element_ozonfresh_text(Fresh.VAIUE_RECIRES)
        assert text == "Рецепты"

    def test_breakfasts(self, ozon):
        ozon.open_ozon()
        ozon.click_to_tabs_ozonfresh(Fresh.BREAKFASTS)
        text = ozon.get_element_ozonfresh_text(Fresh.BREAKFASTS)
        assert text == "Завтраки"

    def test_first_meal(self, ozon):
        ozon.open_ozon()
        ozon.click_to_tabs_ozonfresh(Fresh.FIRST_MEAL)
        text = ozon.get_element_ozonfresh_text(Fresh.FIRST_MEAL)
        assert text == "Первые блюда"

    def test_second_courses(self, ozon):
        ozon.open_ozon()
        ozon.click_to_tabs_ozonfresh(Fresh.SECOND_DISHES)
        text = ozon.get_element_ozonfresh_text(Fresh.SECOND_DISHES)
        assert text == "Вторые блюда"

    def test_salads(self, ozon):
        ozon.open_ozon()
        ozon.click_to_tabs_ozonfresh(Fresh.SALADS)
        text = ozon.get_element_ozonfresh_text(Fresh.SALADS)
        assert text == "Салаты"

    def test_snacks(self, ozon):
        ozon.open_ozon()
        ozon.click_to_tabs_ozonfresh(Fresh.CNACKS)
        text = ozon.get_element_ozonfresh_text(Fresh.CNACKS)
        assert text == "Закуски"

    def test_desserts(self, ozon):
        ozon.open_ozon()
        ozon.click_to_tabs_ozonfresh(Fresh.DESSERTS)
        text = ozon.get_element_ozonfresh_text(Fresh.DESSERTS)
        assert text == "Десерты"


    def test_from_different_countries(self, ozon):
        ozon.open_ozon()
        ozon.click_to_tabs_ozonfresh(Fresh.COUNTRIES)
        text = ozon.get_element_ozonfresh_text(Fresh.COUNTRIES)
        assert text == "Из разных стран"


    def test_stock(self, ozon):
        ozon.click_to_tabs_ozonfresh(Fresh.OZON_FRESH)
        ozon.click_to_tabs_ozonfresh(Fresh.STOCK)
        text = ozon.get_element_ozonfresh_text(Fresh.VALUE_CTOCK)
        assert text == "Набор стаканов для воды Vivo, 320 мл"


    def test_sezon(self, ozon):
        ozon.click_to_tabs_ozonfresh(Fresh.OZON_FRESH)
        ozon.click_to_tabs_ozonfresh(Fresh.SEZON)
        text = ozon.get_element_ozonfresh_text(Fresh.SEASONAL_OFFER)
        assert text == "Сезонное предложение!"