from selenium.webdriver.common.by import By


class OzonGastronomysLocators:
    HEALTHY_LIFESTYLE_FRESH = (
    By.XPATH, "//a[@href='/highlight/gastronomiya-ozon-express-302368/?miniapp=supermarket&category=9990000']")
    HEALTHY_LIFESTYLE_FRESH_VALUE = (By.XPATH, "//span[contains(text(), 'Хумус Ozon fresh, со свеклой, 160 г')]")
    MEAT_POUITRY_FISH = (
    By.XPATH, "//a[@href='/highlight/gastronomiya-ozon-express-302368/?miniapp=supermarket&category=9971000']")
    MEAT_POUITRY_FISH_VALUE = (By.XPATH, "//a[contains(text(), 'Колбасы и деликатесы')]")
    PREPARED_FOOD = (
    By.XPATH, "//a[@href='/highlight/gastronomiya-ozon-express-302368/?miniapp=supermarket&category=9521000']")
    PREPARED_FOOD_VALUE = (By.XPATH, "//a[contains(text(), 'Салаты и закуски')]")
    FROZEN_FOOD = (
    By.XPATH, "//a[@href='/highlight/gastronomiya-ozon-express-302368/?miniapp=supermarket&category=9437000']")
    FROZEN_FOOD_VALUE = (By.XPATH, "//a[contains(text(), 'Полуфабрикаты')]")
    GROCERY = (
    By.XPATH, "//a[@href='/highlight/gastronomiya-ozon-express-302368/?miniapp=supermarket&category=30701000']")
    GROCERY_VALUE = (By.XPATH, "//a[contains(text(), 'Консервы')]")
    GROCERY_G = (By.XPATH, "//a[contains(text(), 'Бакалея')]")
    BATTER_SAUCES_KETCHUPS_VALUE = (By.XPATH, "//a[contains(text(), 'Масло, соусы, кетчупы')]")