import time

import pytest

from locators.pet_supplies_locators import OzonPetSuppliesLocators as Pet


class TestPetSupplies:
    @pytest.mark.parametrize('locator, locator_text, text_to_check', [
        (Pet.HYGIENE_CARE, Pet.HYGIENE_CARE_VALUE, 'Гигиена для животных'),
        (Pet.PRODUCTS_CATS, Pet.PRODUCTS_CATS_VALUE, 'Товары для кошек'),
        (Pet.PRODUCTS_DOGS, Pet.PRODUCTS_DOGS_VALUE, 'Товары для собак'),
        (Pet.PRODUCTS_RODENTS, Pet.PRODUCTS_RODENTS_VALUE, 'Товары для грызунов'),
        (Pet.PRODUCTS_BIRDS, Pet.PRODUCTS_BIRDS_VALUE, 'Корм для птиц'),
        (Pet.PRODUCTS_FISH, Pet.PRODUCTS_FISH_VALUE, 'Товары для рыб'),

    ])
    def test_pet_supplies(self, ozon_pet_supplies, locator, locator_text, text_to_check):
        ozon_pet_supplies.open_pet_supplies()
        ozon_pet_supplies.click_to_tabs_pet_supplies(locator)
        text = ozon_pet_supplies.get_element_pet_supplies_text(locator_text)
        assert text == text_to_check

    @pytest.mark.parametrize('locator, locator_text, text_to_check', [
        (Pet.ROYAL_CANIN, Pet.ROYAL_CANIN_VALUE, 'Товары для животных Royal Canin'),
        (Pet.PRO_PLAN, Pet.PRO_PLAN_VALUE, 'Товары для животных Pro Plan'),
        (Pet.PI_PI_BENT, Pet.PI_PI_BENT_VALUE, 'Товары для животных Pi-Pi-Bent'),
        (Pet.MORGE, Pet.MORGE_VALUE, 'Товары для животных Monge'),

    ])
    def test_tab_brend(self, ozon_pet_supplies, locator, locator_text, text_to_check):
        ozon_pet_supplies.open_pet_supplies()
        ozon_pet_supplies.click_to_tabs_pet_supplies(locator)
        text = ozon_pet_supplies.get_element_pet_supplies_text(locator_text)
        assert text == text_to_check
