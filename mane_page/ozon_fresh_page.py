from locators.ozon_fresh_locators import OzonFreshPageLocators
from mane_page.base_page import BasePage
from mane_page.recipes_page import OzonRecipesPage


class OzonFreshPage(BasePage):

    def open_recipes_page(self):
        return OzonRecipesPage(self.driver).open_recipes()

