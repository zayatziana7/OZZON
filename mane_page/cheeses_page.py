from locators.ozon_fresh_locators import OzonFreshPageLocators
from locators.products_locators import OzonProductsLocatorss
from mane_page.base_page import BasePage


class OzonCheesesPage(BasePage):

    def click_to_tabs_cheeses(self, locator):
        self.find_element_and_click_via_script(locator)

    def get_element_cheeses_text(self, locator):
        element = self.wait_presence_of_element_located(locator)
        return element.text

    def open_tab_cheeses(self):
        self.click_to_tabs_cheeses(OzonFreshPageLocators.OZON_FRESH)
        self.click_to_tabs_cheeses(OzonFreshPageLocators.PRODUCTS)
        self.click_to_tabs_cheeses(OzonProductsLocatorss.CHEESES)
