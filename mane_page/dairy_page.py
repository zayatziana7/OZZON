from locators.ozon_fresh_locators import OzonFreshPageLocators
from locators.products_locators import OzonProductsLocatorss
from mane_page.base_page import BasePage


class OzonDairyPage(BasePage):

    def click_to_tabs_dairy(self, locator):
        self.find_element_and_click_via_script(locator)

    def get_element_dairy_text(self, locator):
        element = self.wait_presence_of_element_located(locator)
        return element.text

    def test_open_dairy(self):
        self.click_to_tabs_dairy(OzonFreshPageLocators.OZON_FRESH)
        self.click_to_tabs_dairy(OzonFreshPageLocators.PRODUCTS)
        self.click_to_tabs_dairy(OzonProductsLocatorss.DAIRY)
