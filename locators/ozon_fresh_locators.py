from selenium.webdriver.common.by import By


class OzonFreshPageLocators:
    OZON_FRESH = (By.XPATH, "//a[@href='/category/supermarket-25000/']")
    FRESH = (By.XPATH, "//div[@class='oaa0 oa0a']")
    RECIPES = (By.CSS_SELECTOR, 'a[href^="/recipe/"]')
    VAIUE_RECIRES = (By.XPATH, "//h1[contains(text(), 'Рецепты')]")
    BREAKFASTS = (By.XPATH, "//span[contains(text(), 'Завтраки')]")
    FIRST_MEAL = (By.XPATH, "//span[contains(text(), 'Первые блюда')]")
    SECOND_DISHES = (By.XPATH, "//span[contains(text(), 'Вторые блюда')]")
    SALADS = (By.XPATH, "//span[contains(text(), 'Салаты')]")
    CNACKS = (By.XPATH, "//span[contains(text(), 'Закуски')]")
    DESSERTS = (By.XPATH, "//span[contains(text(), 'Десерты')]")
    COUNTRIES = (By.XPATH, "//span[contains(text(), 'Из разных стран')]")
    STOCK = (By.CSS_SELECTOR, 'a[href^="/highlight/vse-aktsii-ozon-express-161703/?miniapp=supermarket"]')
    VALUE_CTOCK = (By.XPATH, "//span[contains(text(), 'Набор стаканов для воды Vivo, 320 мл')]")
    SEZON = (By.CSS_SELECTOR, 'a[href^="/highlight/sezonnoe-predlozhenie-538624/?miniapp=supermarket"]')
    SEASONAL_OFFER = (By.XPATH, "//h1[contains(text(), 'Сезонное предложение!')]")
    PRODUCTS = (By.CSS_SELECTOR, 'a[href^="/highlight/produktsiya-ozon-express-199745/?miniapp=supermarket"]')
    OUR_PRODUCTS = (By.XPATH, "//h2[contains(text(), 'Наши продукты')]")
    MOTHERS = (By.CSS_SELECTOR, 'a[href^="/category/supermarket-tovary-dlya-mam-i-detey-7000000/?miniapp=supermarket"]')
    MOTHERS_AND_CHILDREN = (By.XPATH, "//h1[@class='ie5']")
    BEAUTY = (By.CSS_SELECTOR, 'a[href^="/category/supermarket-krasota-i-zdorove-6500000/?miniapp=supermarket"]')
    BEAUTY_AND_HEALTH = (By.XPATH, "//h1[@class='je']")
    HOME = (By.CSS_SELECTOR, 'a[href^="/category/supermarket-dom-i-sad-14500000/?miniapp=supermarket"]')
    HOME_AND_GARDEN = (By.XPATH, "//h1[@class='ie5']")

