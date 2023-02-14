import time

import pytest
from selenium.webdriver import ActionChains
from hamcrest import assert_that, equal_to, greater_than
from locators.pet_supplies_locators import OzonPetSuppliesLocators as Pet


class TestPetSupplies:
    @pytest.mark.parametrize('locator, locator_text, text_to_check, url', [
        (Pet.HYGIENE_CARE, Pet.HYGIENE_CARE_VALUE, 'Гигиена для животных', 'gigiena-dlya-zhivotnyh'),
        (Pet.PRODUCTS_CATS, Pet.PRODUCTS_CATS_VALUE, 'Товары для кошек', 'dlya-koshek'),
        (Pet.PRODUCTS_DOGS, Pet.PRODUCTS_DOGS_VALUE, 'Товары для собак', 'dlya-sobak'),
        (Pet.PRODUCTS_RODENTS, Pet.PRODUCTS_RODENTS_VALUE, 'Товары для грызунов', 'dlya-gryzunov'),
        (Pet.PRODUCTS_BIRDS, Pet.PRODUCTS_BIRDS_VALUE, 'Корм для птиц', 'dlya-ptits'),
        (Pet.PRODUCTS_FISH, Pet.PRODUCTS_FISH_VALUE, 'Товары для рыб', 'dlya-ryb'),

    ])
    def test_pet_supplies(self, ozon_pet_supplies, locator, locator_text, text_to_check, url):
        ozon_pet_supplies.open_pet_supplies()
        ozon_pet_supplies.click_to_tabs_pet_supplies(locator)
        text = ozon_pet_supplies.get_element_pet_supplies_text(locator_text)
        current_url = ozon_pet_supplies.get_current_url()
        assert text == text_to_check
        assert url in current_url, f'{url} нет в {current_url}'

    @pytest.mark.parametrize('locator, locator_text, text_to_check, url',  [
        (Pet.ROYAL_CANIN, Pet.ROYAL_CANIN_VALUE, 'Товары для животных Royal Canin', 'royal-canin'),
        (Pet.PRO_PLAN, Pet.PRO_PLAN_VALUE, 'Товары для животных Pro Plan', 'pro-plan'),
        (Pet.PI_PI_BENT, Pet.PI_PI_BENT_VALUE, 'Товары для животных Pi-Pi-Bent', 'pi-pi-bent'),
        (Pet.MORGE, Pet.MORGE_VALUE, 'Товары для животных Monge', 'monge'),

    ])
    def test_tab_brend(self, ozon_pet_supplies, locator, locator_text, text_to_check, url):
        ozon_pet_supplies.open_pet_supplies()
        ozon_pet_supplies.click_to_tabs_pet_supplies(locator)
        text = ozon_pet_supplies.get_element_pet_supplies_text(locator_text)
        current_url = ozon_pet_supplies.get_current_url()
        assert_that(text, equal_to(text_to_check), 'проверка не сошлась')
        assert url in current_url, f'{url} нет в {current_url}'


    @pytest.mark.skip('не кликает по пункту')
    @pytest.mark.parametrize('locator, locator_text', [
        (Pet.OO, Pet.OO_OO),

    ])
    def test_kind_of_animal(self, ozon_pet_supplies, locator, locator_text):
        ozon_pet_supplies.open_pet_supplies()
        element = ozon_pet_supplies.driver.find_element(*locator)
        actions = ActionChains(ozon_pet_supplies.driver)
        actions.move_to_element(element).send_keys('Новинки')
        ozon_pet_supplies.find_element_and_click_via_action_chains(locator).send_keys('Новинки')
        ozon_pet_supplies.find_element_and_click_via_action_chains(locator_text)



    @pytest.mark.parametrize('locator, locator_text, text_to_check, url, price',  [
        (Pet.ROYAL_CANIN, Pet.ROYAL_CANIN_VALUE, 'Товары для животных Royal Canin', 'royal-canin', '105 товаров'),
        # (Pet.PRO_PLAN, Pet.PRO_PLAN_VALUE, 'Товары для животных Pro Plan', 'pro-plan'),
        # (Pet.PI_PI_BENT, Pet.PI_PI_BENT_VALUE, 'Товары для животных Pi-Pi-Bent', 'pi-pi-bent'),
        # (Pet.MORGE, Pet.MORGE_VALUE, 'Товары для животных Monge', 'monge'),

    ])
    def test_tab_brend(self, ozon_pet_supplies, locator, locator_text, text_to_check, url, price):
        ozon_pet_supplies.open_pet_supplies()
        ozon_pet_supplies.click_to_tabs_pet_supplies(locator)
        text = ozon_pet_supplies.get_element_pet_supplies_text(locator_text)
        current_url = ozon_pet_supplies.get_current_url()
        assert_that(text, equal_to(text_to_check), 'проверка не сошлась')
        assert url in current_url, f'{url} нет в {current_url}'

