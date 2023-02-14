import pytest

from locators.mothers_children_locators import OzonMothersChildrenLocators as Mothers
from hamcrest import assert_that, equal_to, greater_than

class TestMothersChildren:

    def test_mothers_and_children(self, ozon_mothers_children):
        ozon_mothers_children.open_mothers_children()
        text = ozon_mothers_children.get_element_mothers_children_text(Mothers.MOTHERS_AND_CHILDREN)
        assert text == "Товары для мам и детей"
        assert_that(text, equal_to("Товары для мам и детей"), 'проверка не сошлась')


    @pytest.mark.parametrize('locator, locator_text, text_to_check', [
        (Mothers.TOYS_AND_GAMES, Mothers.TOYS_AND_GAMES_VALUE, 'Игрушки и игры'),
        (Mothers.CHILDREN_FOOD, Mothers.CHILDREN_FOOD_VALUE, 'Детское питание'),
        (Mothers.DIAPETS_AND_CARE, Mothers.DIAPETS_AND_CARE_VALUE, 'Детская гигиена и уход'),
        (Mothers.FEEDING_AND_ELECTRONICS, Mothers.FEEDING_ELECTRONICS_VALUE,
         'Все товары по акции уже купили. Возможно, вам будут интересны другие предложения'),
        (Mothers.FOR_MOMS, Mothers.FOR_MOMS_VALUE, 'Товары для мам')
    ])
    def test_mothers_children_tab(self, ozon_mothers_children, locator, locator_text, text_to_check):
        ozon_mothers_children.open_mothers_children()
        ozon_mothers_children.click_to_tabs_mothers_children(locator)
        text = ozon_mothers_children.get_element_mothers_children_text(locator_text)
        assert_that(text, equal_to(text_to_check), 'проверка не сошлась')

    def test_clothes_and_accessories(self, ozon_mothers_children):
        ozon_mothers_children.open_mothers_children()
        ozon_mothers_children.click_to_tabs_mothers_children(Mothers.CLOTHES_ACCESSORIES)
        ozon_mothers_children.click_to_tabs_mothers_children(Mothers.CLOTHES_ACCESSORIES_C)
        text = ozon_mothers_children.get_element_mothers_children_text(Mothers.CLOTHES_ACCESSORIES_VALUE)
        assert text == 'Сумки, рюкзаки, аксессуары'
        assert_that(text, equal_to('Сумки, рюкзаки, аксессуары'), 'проверка не сошлась')
