from locators.ozon_fresh_locators import OzonFreshPageLocators
from mane_page.base_page import BasePage


class OzonRecipesPage(BasePage):
    def open_recipes(self):
        """
        Открывает вкладку с акциями
        :return:
        """
        return self.find_element_and_click_via_script(OzonFreshPageLocators.RECIPES)

