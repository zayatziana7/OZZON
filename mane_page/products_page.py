from locators.ozon_fresh_locators import OzonFreshPageLocators as Ozon
from mane_page.base_page import BasePage


class OzonProductsPage(BasePage):

    def click_to_tabs_products(self, locator):
        self.find_element_and_click_via_script(locator)

    def get_element_products_text(self, locator):
        element = self.wait_presence_of_element_located(locator)
        return element.text

    def open_products(self):
        self.click_to_tabs_products(Ozon.OZON_FRESH)
        self.click_to_tabs_products(Ozon.PRODUCTS)
