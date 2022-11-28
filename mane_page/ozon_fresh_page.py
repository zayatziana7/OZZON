from locators.ozon_fresh_locators import OzonFreshPageLocators
from mane_page.base_page import BasePage


class OzonPages(BasePage):

    def click_to_tabs_ozonfresh(self, locator):
        self.find_element_and_click_via_script(locator)

    def get_element_ozonfresh_text(self, locator):
        element = self.wait_presence_of_element_located(locator)
        return element.text

    def open_ozon(self):
        self.click_to_tabs_ozonfresh(OzonFreshPageLocators.OZON_FRESH)
        self.click_to_tabs_ozonfresh(OzonFreshPageLocators.RECIPES)
