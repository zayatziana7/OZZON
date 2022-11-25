from locators.chees_locators import OzonCheesesLocators as Cheeses


class TestCheeses:
    def test_add_to_cart_cream_cheese(self, ozon_cheeses):
        ozon_cheeses.open_tab_cheeses()
        ozon_cheeses.click_to_tabs_cheeses(Cheeses.CREAM_CHEESE)
        text = ozon_cheeses.get_element_cheeses_text(Cheeses.CREAM_CHEESE_VALUE)
        assert text == "Сыр Сливочный Ozon fresh, 50%, 200 г"

    def test_dutch_cheese(self, ozon_cheeses):
        ozon_cheeses.open_tab_cheeses()
        ozon_cheeses.click_to_tabs_cheeses(Cheeses.DUTCH_CHEESE)
        text = ozon_cheeses.get_element_cheeses_text(Cheeses.DUTCH_CHEESE_VALUE)
        assert text == "Сыр Голландский Ozon fresh, 45%, нарезка, 125 г"

    def test_cheese_with_herbs(self, ozon_cheeses):
        ozon_cheeses.open_tab_cheeses()
        ozon_cheeses.click_to_tabs_cheeses(Cheeses.CHEESE_WITH_HERBS)
        text = ozon_cheeses.get_element_cheeses_text(Cheeses.CHEESE_WITH_HERBS_VALUE)
        assert text == 'Сыр с пряными травами Ozon fresh, 50%, 200 г'

    def test_cheese_with_tomato_and_basil(self, ozon_cheeses):
        ozon_cheeses.open_tab_cheeses()
        ozon_cheeses.click_to_tabs_cheeses(Cheeses.CHEESE_WITH_TOMATO_BASIL)
        text = ozon_cheeses.get_element_cheeses_text(Cheeses.CHEESE_WITH_TOMATO_BASIL_VALUE)
        assert text == 'Сыр с томатом и базиликом Ozon fresh, 50%, нарезка, 125 г'

    def test_tilsiter_cheese(self, ozon_cheeses):
        ozon_cheeses.open_tab_cheeses()
        ozon_cheeses.click_to_tabs_cheeses(Cheeses.TIILSITER_CHEESE)
        text = ozon_cheeses.get_element_cheeses_text(Cheeses.TIILSITER_CHEESE_VALUE)
        assert text == 'Сыр Тильзитер Ozon fresh, 45%, 200 г'

    def test_hard_cheese_palermo(self, ozon_cheeses):
        ozon_cheeses.open_tab_cheeses()
        ozon_cheeses.click_to_tabs_cheeses(Cheeses.HARD_CHEESE_PALERMO)
        text = ozon_cheeses.get_element_cheeses_text(Cheeses.HARD_CHEESE_PALERMO_VALUE)
        assert text == 'Сыр твердый Palermo Ozon fresh, 40%, 180 г'

    def test_chees_feta(self, ozon_cheeses):
        ozon_cheeses.open_tab_cheeses()
        ozon_cheeses.click_to_tabs_cheeses(Cheeses.CHEES_FETA)
        text = ozon_cheeses.get_element_cheeses_text(Cheeses.CHEES_FETA_VALUE)
        assert text == 'Сыр Фета Ozon fresh, 45%, рассольный, 200 г'

    def test_burrata_cheese(self, ozon_cheeses):
        ozon_cheeses.open_tab_cheeses()
        ozon_cheeses.click_to_tabs_cheeses(Cheeses.BURRATA_CHEESE)
        text = ozon_cheeses.get_element_cheeses_text(Cheeses.BURRATA_CHEESE_VALUE)
        assert text == 'Сыр Буррата Ozon fresh, 50%, 125 г'

    def test_cheese_mozzarella_mini(self, ozon_cheeses):
        ozon_cheeses.open_tab_cheeses()
        ozon_cheeses.click_to_tabs_cheeses(Cheeses.CHEESE_MOZZARELLA_MINI)
        text = ozon_cheeses.get_element_cheeses_text(Cheeses.CHEESE_MOZZARELLA_MINI_VALUE)
        assert text == 'Сыр Моцарелла Мини Ozon fresh, 50%, 100 г'

    def test_hard_cheese_palermo_solid(self, ozon_cheeses):
        ozon_cheeses.open_tab_cheeses()
        ozon_cheeses.click_to_tabs_cheeses(Cheeses.HARD_CHEESE_PALERMO_SOLID)
        text = ozon_cheeses.get_element_cheeses_text(Cheeses.HARD_CHEESE_PALERMO_SOLID_VALUE)
        assert text == 'Сыр твердый Palermo Ozon fresh, 40%, 180 г'

    def test_pickled_cheese_brynza(self, ozon_cheeses):
        ozon_cheeses.open_tab_cheeses()
        ozon_cheeses.click_to_tabs_cheeses(Cheeses.PICKLED_CHESEE_BRYNZA)
        text = ozon_cheeses.get_element_cheeses_text(Cheeses.PICKLED_CHESEE_BRYNZA_VALUE)
        assert text == 'Сыр рассольный Брынза Ozon fresh, 30%, 250г'

    def test_cheese_russian(self, ozon_cheeses):
        ozon_cheeses.open_tab_cheeses()
        ozon_cheeses.click_to_tabs_cheeses(Cheeses.CHEESE_RUSSIAN)
        text = ozon_cheeses.get_element_cheeses_text(Cheeses.CHEESE_RUSSIAN_VALUE)
        assert text == 'Сыр Российский Ozon fresh, 45%, 200 г'
