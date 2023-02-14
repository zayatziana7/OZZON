from locators.house_garden_locators import OzonHouseGardenLocators as Home
from hamcrest import assert_that, equal_to, greater_than

class TestHouseGarden:

    def test_house_and_garden(self, ozon_house_garden):
        ozon_house_garden.click_to_tabs_house_garden(Home.HOUSEGARDEN)
        text = ozon_house_garden.get_element_house_garden_text(Home.HOUSEGARDEN_VALUE)
        assert_that(text, equal_to("Дом и сад"), 'проверка не сошлась')

    def test_flowers_with_delivery(self, ozon_house_garden):
        ozon_house_garden.click_to_tabs_house_garden(Home.HOUSEGARDEN)
        ozon_house_garden.click_to_tabs_house_garden(Home.FLOWERS_DELIVERY)
        text = ozon_house_garden.get_element_house_garden_text(Home.FLOWERS_DELIVERY_VALUE)
        assert_that(text, equal_to("Букеты цветов"), 'проверка не сошлась')