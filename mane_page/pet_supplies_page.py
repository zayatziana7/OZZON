from locators.ozon_fresh_locators import OzonFreshPageLocators
from locators.pet_supplies_locators import OzonPetSuppliesLocators
from mane_page.base_page import BasePage


class OzonPetSuppliesPage(BasePage):

    def click_to_tabs_pet_supplies(self, locator):
        self.find_element_and_click_via_script(locator)

    def get_element_pet_supplies_text(self, locator):
        element = self.wait_presence_of_element_located(locator)
        return element.text

    def open_pet_supplies(self):
        self.click_to_tabs_pet_supplies(OzonPetSuppliesLocators.PET_SUPPLIES)