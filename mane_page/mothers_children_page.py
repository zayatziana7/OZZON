from locators.ozon_fresh_locators import OzonFreshPageLocators
from mane_page.base_page import BasePage


class OzonMothersСhildrenPage(BasePage):

    def click_to_tabs_mothers_children(self, locator):
        self.find_element_and_click_via_script(locator)

    def get_element_mothers_children_text(self, locator):
        element = self.wait_presence_of_element_located(locator)
        return element.text

    def open_mothers_children(self):
        self.click_to_tabs_mothers_children(OzonFreshPageLocators.MOTHERS)
