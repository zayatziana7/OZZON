import pytest

from locators.chees_locators import OzonCheesesLocators as Cheeses


class TestCheeses:

    @pytest.mark.parametrize('locator, locator_text, text_to_check', [
        (Cheeses.CREAM_CHEESE, Cheeses.CREAM_CHEESE_VALUE, "Сыр Сливочный Ozon fresh, 50%, 200 г"),
        (Cheeses.DUTCH_CHEESE, Cheeses.DUTCH_CHEESE_VALUE, "Сыр Голландский Ozon fresh, 45%, нарезка, 125 г"),
        (Cheeses.CHEESE_WITH_HERBS, Cheeses.CHEESE_WITH_HERBS_VALUE, 'Сыр с пряными травами Ozon fresh, 50%, 200 г'),
        (Cheeses.CHEESE_WITH_TOMATO_BASIL, Cheeses.CHEESE_WITH_TOMATO_BASIL_VALUE,
         'Сыр с томатом и базиликом Ozon fresh, 50%, нарезка, 125 г'),
        (Cheeses.TIILSITER_CHEESE, Cheeses.TIILSITER_CHEESE_VALUE, 'Сыр Тильзитер Ozon fresh, 45%, 200 г'),
        (Cheeses.HARD_CHEESE_PALERMO, Cheeses.HARD_CHEESE_PALERMO_VALUE, 'Сыр твердый Palermo Ozon fresh, 40%, 180 г'),
        (Cheeses.CHEES_FETA, Cheeses.CHEES_FETA_VALUE, 'Сыр Фета Ozon fresh, 45%, рассольный, 200 г'),
        (Cheeses.BURRATA_CHEESE, Cheeses.BURRATA_CHEESE_VALUE, 'Сыр Буррата Ozon fresh, 50%, 125 г'),
        (Cheeses.CHEESE_MOZZARELLA_MINI, Cheeses.CHEESE_MOZZARELLA_MINI_VALUE, 'Сыр Моцарелла Мини Ozon fresh, 50%, 100 г'),
        (Cheeses.HARD_CHEESE_PALERMO_SOLID, Cheeses.HARD_CHEESE_PALERMO_SOLID_VALUE, 'Сыр твердый Palermo Ozon fresh, 40%, 180 г'),
        (Cheeses.PICKLED_CHESEE_BRYNZA, Cheeses.PICKLED_CHESEE_BRYNZA_VALUE, 'Сыр рассольный Брынза Ozon fresh, 30%, 250г'),
        (Cheeses.CHEESE_RUSSIAN, Cheeses.CHEESE_RUSSIAN_VALUE, 'Сыр Российский Ozon fresh, 45%, 200 г'),

    ])
    def test_add_to_cart_cream_cheese(self, ozon_cheeses, locator, locator_text, text_to_check):
        ozon_cheeses.open_tab_cheeses()
        ozon_cheeses.click_to_tabs_cheeses(locator)
        text = ozon_cheeses.get_element_cheeses_text(locator_text)
        assert text == text_to_check
