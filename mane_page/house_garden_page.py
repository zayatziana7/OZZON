from mane_page.base_page import BasePage


class OzonHouseGardenPage(BasePage):

    def click_to_tabs_house_garden(self, locator):
        self.find_element_and_click_via_script(locator)

    def get_element_house_garden_text(self, locator):
        element = self.wait_presence_of_element_located(locator)
        return element.text
