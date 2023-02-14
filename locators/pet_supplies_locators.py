from selenium.webdriver.common.by import By


class OzonPetSuppliesLocators:
    PET_SUPPLIES =(By.CSS_SELECTOR, 'a[href^="/category/supermarket-tovary-dlya-zhivotnyh-12300000/?miniapp=supermarket"]')
    HYGIENE_CARE = (By.CSS_SELECTOR, 'a[href^="/category/supermarket-gigiena-dlya-zhivotnyh-30973000/?miniapp=supermarket"]')
    HYGIENE_CARE_VALUE = (By.XPATH, "//h1[contains(text(), 'Гигиена для животных')]")
    PRODUCTS_CATS = (By.CSS_SELECTOR, 'a[href^="/category/supermarket-dlya-koshek-12347000/?miniapp=supermarket"]')
    PRODUCTS_CATS_VALUE = (By.XPATH, "//h1[contains(text(), 'Товары для кошек')]")
    PRODUCTS_DOGS =(By.CSS_SELECTOR, 'a[href^="/category/supermarket-dlya-sobak-12301000/?miniapp=supermarket"]')
    PRODUCTS_DOGS_VALUE = (By.XPATH, "//h1[contains(text(), 'Товары для собак')]")
    PRODUCTS_RODENTS = (By.CSS_SELECTOR, 'a[href^="/category/supermarket-dlya-gryzunov-12429000/?miniapp=supermarket"]')
    PRODUCTS_RODENTS_VALUE = (By.XPATH, "//h1[contains(text(), 'Товары для грызунов')]")
    PRODUCTS_BIRDS= (By.CSS_SELECTOR, 'a[href^="/category/korm-dlya-ptits-12430000/?miniapp=supermarket"]')
    PRODUCTS_BIRDS_VALUE = (By.XPATH, "//h1[contains(text(), 'Корм для птиц')]")
    PRODUCTS_FISH = (By.CSS_SELECTOR, 'a[href^="/category/dlya-ryb-1251000/?miniapp=supermarket"]')
    PRODUCTS_FISH_VALUE = (By.XPATH, "//h1[contains(text(), 'Товары для рыб')]")
    ROYAL_CANIN = (By.CSS_SELECTOR, 'a[href^="/category/supermarket-tovary-dlya-zhivotnyh-12300000/?miniapp=supermarket&brand=19060364"]')
    ROYAL_CANIN_VALUE = (By.XPATH, "//h1[contains(text(), 'Товары для животных Royal Canin')]")
    PRO_PLAN = (By.CSS_SELECTOR, 'a[href^="/category/supermarket-tovary-dlya-zhivotnyh-12300000/?miniapp=supermarket&brand=7610736"]')
    PRO_PLAN_VALUE = (By.XPATH, "//h1[contains(text(), 'Товары для животных Pro Plan')]")
    PI_PI_BENT = (By.CSS_SELECTOR, 'a[href^="/category/supermarket-tovary-dlya-zhivotnyh-12300000/?miniapp=supermarket&brand=7374393"]')
    PI_PI_BENT_VALUE = (By.XPATH, "//h1[contains(text(), 'Товары для животных Pi-Pi-Bent')]")
    MORGE = (By.CSS_SELECTOR, 'a[href^="/category/supermarket-tovary-dlya-zhivotnyh-12300000/?miniapp=supermarket&brand=31266274"]')
    MORGE_VALUE = (By.XPATH, "//h1[contains(text(), 'Товары для животных Monge')]")
    OO = (By.XPATH, "//input[@role='combobox']")
    OO_OO = (By.XPATH, "//div[contains(text(), 'Новинки')]")
    WE = (By.XPATH, "//span[contains(text(), '105 товаров')]")



