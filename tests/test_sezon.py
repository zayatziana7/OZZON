import time

import pytest

from locators.sezon_locators import OzonSezonLocators as Sezon


class TestSezon:
    def test_sezon(self, ozon_sezon):
        ozon_sezon.open_sezon()
        text = ozon_sezon.get_element_sezon_text(Sezon.VEGETABLES_FRUITS_VALUE)
        assert text == 'Мандарины Турция, 1 кг'

    @pytest.mark.parametrize('locator, locator_text, text_to_check', [
        (Sezon.TANGERINES, Sezon.TANGERINES_VALUE, 'Мандарины Турция, 1 кг'),
        (Sezon.QUINCE, Sezon.QUINCE_VALUE, 'Айва, ароматная, множество витаминов, Узбекистан, 2 шт'),
        (Sezon.POMEGRANATE, Sezon.POMEGRANATE_VALUE, 'Гранат отборный, новый урожай, 1 шт'),
        (Sezon.TANGERINES_MINI, Sezon.TANGERINES_MINI_VALUE, 'Мандарины мини с зеленцой, 500 г'),
        (Sezon.GRAPE, Sezon.GRAPE_VALUE, 'Виноград Киш-Миш, без косточек, 500 г'),
        (Sezon.PERSIMMON_KOROLEK, Sezon.PERSIMMON_KOROLEK_VALUE, 'Хурма Королек, осенняя, с зелеными бочками, 1 кг'),
        (Sezon.PINEAPPLE, Sezon.PINEAPPLE_VALUE, 'Ананас, 1 шт'),
        (Sezon.WATERMEION_MINI, Sezon.WATERMEION_MINI_VALUE, 'Арбуз мини красный, с мягкими косточками, 1 шт'),
        (Sezon.GRANBERRY, Sezon.GRANBERRY_VALUE, 'Клюква свежая, витаминная, 250 г'),
        (Sezon.ASPARAGUS, Sezon.ASPARAGUS_VALUE, 'Спаржа зеленая Artfruit, 250 г'),

    ])
    def test_tangerines(self, ozon_sezon, locator, locator_text, text_to_check):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(locator)
        text = ozon_sezon.get_element_sezon_text(locator_text)
        assert text == text_to_check



    def test_reviews(self, ozon_sezon):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(Sezon.ASPARAGUS)
        ozon_sezon.click_to_tabs_sezon(Sezon.REVIEWS)
        text = ozon_sezon.get_element_sezon_text(Sezon.REVIEWS_VALUE)
        assert text == 'Отзывы'


    # def test_question_asparagus(self, ozon_sezon):
    #     ozon_sezon.open_sezon()
    #     ozon_sezon.wait_element(Sezon.ASPARAGUS)
    #     ozon_sezon.wait_element(Sezon.QUESTION_ASPARAGUS)
    #     time.sleep(5)
    #     text = ozon_sezon.get_element_sezon_text(Sezon.QUESTION_ASPARAGUS_VALUE)
    #     assert text == 'Задайте вопрос о товаре'

    # def test_opis(self, ozon_sezon):
    #     ozon_sezon.open_sezon()
    #     ozon_sezon.click_to_tabs_sezon(Sezon.ASPARAGUS)
    #     ozon_sezon.click_to_tabs_sezon(Sezon.OPIS)
    #     t = ozon_sezon.get_element_sezon_text(Sezon.TT)
    #     time.sleep(8)
    #     assert t =='Характеристики'


    def test_tangerines_video(self, ozon_sezon):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(Sezon.TANGERINES)
        ozon_sezon.click_to_tabs_sezon(Sezon.VIDEO)
        text = ozon_sezon.get_element_sezon_text(Sezon.VIDEO_VALUE)
        assert text =='Фото и видео пользователей 122'

    def test_collections(self, ozon_sezon):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(Sezon.TANGERINES)
        text = ozon_sezon.get_element_sezon_text(Sezon.COLLECTIONS)
        assert text == 'Подборки товаров в категории Цитрусовые'


    @pytest.mark.parametrize('locator, locator_text, text_to_check', [
        (Sezon.QUESTIOS, Sezon.QUESTIOS_VALUE, 'Задайте вопрос о товаре'),
        (Sezon.POMELO, Sezon.POMELO_VALUE, 'Товары не в наличии'),

    ])
    def test_questions(self, ozon_sezon, locator, locator_text, text_to_check):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(Sezon.TANGERINES)
        ozon_sezon.click_to_tabs_sezon(locator)
        text = ozon_sezon.get_element_sezon_text(locator_text)
        assert text == text_to_check



    # def test_e(self, ozon_sezon):
    #     ozon_sezon.open_sezon()
    #     ozon_sezon.click_to_tabs_sezon(Sezon.TANGERINES)
    #     ozon_sezon.click_to_tabs_sezon(Sezon.E)
    #     text = ozon_sezon.get_element_sezon_text(Sezon.E_E)
    #     assert text == 'Узнайте о снижении цены'

    def test_q(self, ozon_sezon):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(Sezon.TANGERINES)
        ozon_sezon.click_to_tabs_sezon(Sezon.Y)
        text = ozon_sezon.get_element_sezon_text(Sezon.Y_Y)
        assert text == 'Введите номер телефона'

    # def test_delivery(self, ozon_sezon):
    #     ozon_sezon.open_sezon()
    #     ozon_sezon.click_to_tabs_sezon(Sezon.TANGERINES)
    #     ozon_sezon.click_to_tabs_sezon(Sezon.DELIVERY)
    #     text = ozon_sezon.get_element_sezon_text(Sezon.DELIVERY_VALUE)
    #     assert text == 'Стоимость доставки'
    #
    def test_oplata(self, ozon_sezon):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(Sezon.TANGERINES)
        ozon_sezon.click_to_tabs_sezon(Sezon.TR)
        ozon_sezon.switch_browser_tab()
        text = ozon_sezon.get_element_sezon_text(Sezon.TU)
        assert text == 'Способы оплаты'


    def test_oo(self, ozon_sezon):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(Sezon.TANGERINES)
        ozon_sezon.find_element_and_click(Sezon.OO)
        time.sleep(6)

    def test_ttt(self, ozon_sezon):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(Sezon.TANGERINES)
        ozon_sezon.find_element_and_click(Sezon.PP)
        time.sleep(300)
















