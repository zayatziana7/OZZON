from locators.ozon_fresh_locators import OzonFreshPageLocators
from locators.products_locators import OzonProductsLocatorss
from mane_page.base_page import BasePage


class OzonGastronomyPage(BasePage):

    def click_to_tabs_gastronomy(self, locator):
        self.find_element_and_click_via_script(locator)

    def get_element_gastronomy_text(self, locator):
        element = self.wait_presence_of_element_located(locator)
        return element.text

    def open_gastronomy(self):
        self.click_to_tabs_gastronomy(OzonFreshPageLocators.PRODUCTS)
        self.click_to_tabs_gastronomy(OzonProductsLocatorss.GASTRONOMY)
