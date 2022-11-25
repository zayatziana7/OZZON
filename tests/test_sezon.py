import time

from locators.sezon_locators import OzonSezonLocators as Sezon


class TestSezon:
    def test_sezon(self, ozon_sezon):
        ozon_sezon.open_sezon()
        text = ozon_sezon.get_element_sezon_text(Sezon.VEGETABLES_FRUITS_VALUE)
        assert text == 'Мандарины Турция, 1 кг'

    def test_tangerines(self, ozon_sezon):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(Sezon.TANGERINES)
        text = ozon_sezon.get_element_sezon_text(Sezon.TANGERINES_VALUE)
        assert text == 'Мандарины Турция, 1 кг'

    def test_quince(self, ozon_sezon):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(Sezon.QUINCE)
        text = ozon_sezon.get_element_sezon_text(Sezon.QUINCE_VALUE)
        assert text == 'Айва, ароматная, множество витаминов, Узбекистан, 2 шт'

    def test_pomegranate(self, ozon_sezon):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(Sezon.POMEGRANATE)
        text = ozon_sezon.get_element_sezon_text(Sezon.POMEGRANATE_VALUE)
        assert text == 'Гранат отборный, новый урожай, 1 шт'

    def test_tangerines_mini(self, ozon_sezon):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(Sezon.TANGERINES_MINI)
        text = ozon_sezon.get_element_sezon_text(Sezon.TANGERINES_MINI_VALUE)
        assert text == 'Мандарины мини с зеленцой, 500 г'

    def test_grape(self, ozon_sezon):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(Sezon.GRAPE)
        text = ozon_sezon.get_element_sezon_text(Sezon.GRAPE_VALUE)
        assert text == 'Виноград Киш-Миш, без косточек, 500 г'

    def test_persimmon_korolek(self, ozon_sezon):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(Sezon.PERSIMMON_KOROLEK)
        text = ozon_sezon.get_element_sezon_text(Sezon.PERSIMMON_KOROLEK_VALUE)
        assert text == 'Хурма Королек, осенняя, с зелеными бочками, 1 кг'

    def test_pineapple(self, ozon_sezon):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(Sezon.PINEAPPLE)
        text = ozon_sezon.get_element_sezon_text(Sezon.PINEAPPLE_VALUE)
        assert text == 'Ананас, 1 шт'

    def test_watermelon_mini(self, ozon_sezon):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(Sezon.WATERMEION_MINI)
        text = ozon_sezon.get_element_sezon_text(Sezon.WATERMEION_MINI_VALUE)
        assert text == 'Арбуз мини красный, с мягкими косточками, 1 шт'

    def test_granberry(self, ozon_sezon):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(Sezon.GRANBERRY)
        text = ozon_sezon.get_element_sezon_text(Sezon.GRANBERRY_VALUE)
        assert text == 'Клюква свежая, витаминная, 250 г'

    def test_asparagus(self, ozon_sezon):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(Sezon.ASPARAGUS)
        text = ozon_sezon.get_element_sezon_text(Sezon.ASPARAGUS_VALUE)
        assert text == 'Спаржа зеленая Artfruit, 250 г'



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

    def test_delivery(self, ozon_sezon):
        ozon_sezon.open_sezon()
        ozon_sezon.click_to_tabs_sezon(Sezon.TANGERINES)
        ozon_sezon.click_to_tabs_sezon(Sezon.DELIVERY)
        text = ozon_sezon.get_element_sezon_text(Sezon.DELIVERY_VALUE)
        assert text == 'Стоимость доставки'





