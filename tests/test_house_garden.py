from locators.house_garden_locators import OzonHouseGardenLocators as Home


class TestHouseGarden:

    def test_house_and_garden(self, ozon_house_garden):
        ozon_house_garden.click_to_tabs_house_garden(Home.HOUSEGARDEN)
        text = ozon_house_garden.get_element_house_garden_text(Home.HOUSEGARDEN_VALUE)
        assert text == "Дом и сад"

    def test_flowers_with_delivery(self, ozon_house_garden):
        ozon_house_garden.click_to_tabs_house_garden(Home.HOUSEGARDEN)
        ozon_house_garden.click_to_tabs_house_garden(Home.FLOWERS_DELIVERY)
        text = ozon_house_garden.get_element_house_garden_text(Home.FLOWERS_DELIVERY_VALUE)
        assert text == "Букеты цветов"