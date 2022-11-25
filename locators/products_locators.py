from selenium.webdriver.common.by import By


class OzonProductsLocatorss:
    DAIRY = (By.XPATH, "//a[@href='/highlight/molochnye-produkty-i-yaytsa-ozon-express-255355/?miniapp=supermarket']")
    DAIRY_VALUE = (By.XPATH, "//h1[contains(text(), 'Молочные продукты и яйца Ozon fresh')]")
    CHEESES = (By.XPATH, "//a[@href='/highlight/syry-ozon-express-253748/?miniapp=supermarket']")
    CHEESES_VALUE = (By.XPATH, "//h1[contains(text(), 'Сыры Ozon fresh')]")
    GASTRONOMY = (By.XPATH, "//a[@href='/highlight/gastronomiya-ozon-express-302368/?miniapp=supermarket']")
    GASTRONOMY_VALUE = (By.XPATH, "//h1[contains(text(), 'Гастрономия Ozon fresh')]")
    GROCERY = (By.XPATH, "//a[@href='/highlight/makarony-i-krupy-ozon-express-355610/?miniapp=supermarket']")
    GROCERY_VALUE = (By.XPATH, "//h1[contains(text(), 'Бакалея Ozon fresh')]")
    SAUCES = (By.XPATH, "//a[@href='/highlight/sousy-dzhemy-i-med-ozon-express-355617/?miniapp=supermarket']")
    SAUCES_VALUE = (By.XPATH, "//h1[contains(text(), 'Соусы, джемы и мёд Ozon fresh')]")
    FROZEN = (By.XPATH,"//a[@href='/highlight/zamorozka-ozon-express-421627/?miniapp=supermarket']")
    FROZEN_FOOD_PRODUCTS = (By.XPATH, "//h1[contains(text(), 'Замороженные продукты Ozon fresh')]")
    SWEETS_SNACKS = (By.XPATH, "//a[@href='/highlight/sneki-i-sladosti-ozon-express-355621/?miniapp=supermarket']")
    SWEETS_SNACKS_VALUE = (By.XPATH, "//h1[contains(text(), 'Снеки и сладости Ozon fresh')]")
    COFFEE_TEA = (By.XPATH, "//a[@href='/highlight/kofe-i-chay-ozon-express-281907/?miniapp=supermarket']")
    COFFEE_TEA_VALUE = (By.XPATH, "//h1[contains(text(), 'Кофе и чай Ozon fresh')]")
    BEVERAGES = (By.XPATH, "//a[@href='/highlight/napitki-ozon-express-268660/?miniapp=supermarket']")
    BEVERAGES_VALUE = (By.XPATH, "//h1[contains(text(), 'Напитки Ozon fresh')]")
    OUR_BARN = (By.XPATH, "//a[@href='/highlight/pekarnya-ozon-fresh-647113/?miniapp=supermarket']")
    OUR_BARN_VALUE = (By.XPATH, "//h1[contains(text(), 'Пекарня Ozon fresh')]")
    OUR_CONFECTIONERY = (By.XPATH, "//a[@href='/highlight/konditerskaya-ozon-fresh-255634/?miniapp=supermarket']")
    OUR_CONFECTIONERY_VALUE = (By.XPATH, "//h1[contains(text(), 'Наша кондитерская')]")
    PREPARED = (By.XPATH, "//a[@href='/category/supermarket-gotovye-blyuda-9521000/ozon-fresh-100226176/?miniapp=supermarket']")
    PREPARED_VALUE = (By.XPATH, "//h1[contains(text(), 'Готовая еда Ozon fresh')]")