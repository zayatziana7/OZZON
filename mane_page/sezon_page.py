from locators.ozon_fresh_locators import OzonFreshPageLocators as Fresh
from locators.sezon_locators import OzonSezonLocators
from mane_page.base_page import BasePage


class OzonSezonPage(BasePage):

    def click_to_tabs_sezon(self, locator):
        self.find_element_and_click_via_script(locator)

    def wait_element(self, locator):
        self.wait_element_to_be_clickable(locator)

    def get_element_sezon_text(self, locator):
        element = self.wait_presence_of_element_located(locator)
        return element.text

    def open_sezon(self):
        self.click_to_tabs_sezon(Fresh.SEZON)
        self.click_to_tabs_sezon(OzonSezonLocators.VEGETABLES_FRUITS)
