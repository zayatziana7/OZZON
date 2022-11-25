from selenium.webdriver.common.by import By


class OzonMothersChildrenLocators:
    MOTHERS_AND_CHILDREN = (By.XPATH, "//h1[contains(text(), 'Товары для мам и детей')]")
    TOYS_AND_GAMES = (By.XPATH, "//a[@href='/category/supermarket-igrushki-i-igry-7108000/?miniapp=supermarket']")
    TOYS_AND_GAMES_VALUE = (By.XPATH, "//h1[contains(text(), 'Игрушки и игры')]")
    CHILDREN_FOOD = (By.XPATH, "//a[@href='/category/supermarket-detskoe-pitanie-7030000/?miniapp=supermarket']")
    CHILDREN_FOOD_VALUE = (By.XPATH, "//h1[contains(text(), 'Детское питание')]")
    DIAPETS_AND_CARE = (By.XPATH, "//a[@href='/highlight/detskaya-gigiena-i-uhod-280136/?miniapp=supermarket']")
    DIAPETS_AND_CARE_VALUE = (By.XPATH, "//h1[contains(text(), 'Детская гигиена и уход')]")
    FEEDING_AND_ELECTRONICS = (By.XPATH, "//a[@href='/highlight/kormlenie-i-elektronika-280138/?miniapp=supermarket']")
    FEEDING_ELECTRONICS_VALUE = (By.XPATH, "//div[contains(text(), 'Все товары по акции уже купили. Возможно, вам будут интересны другие предложения')]")
    FOR_MOMS = (By.XPATH, "//a[@href='/category/supermarket-tovary-dlya-mam-7077000/?miniapp=supermarket']")
    FOR_MOMS_VALUE = (By.XPATH, "//h1[contains(text(), 'Товары для мам')]")
    CLOTHES_ACCESSORIES = (By.XPATH,"//a[@href='/category/supermarket-odezhda-obuv-i-aksessuary-7500000/?ageo=33940&miniapp=supermarket&sexmaster=135532%2C135533']")
    CLOTHES_ACCESSORIES_C = (By.XPATH, "//a[@href='/category/supermarket-odezhda-obuv-i-aksessuary-7500000/?miniapp=supermarket']")
    CLOTHES_ACCESSORIES_VALUE = (By.XPATH, "//span[contains(text(), 'Сумки, рюкзаки, аксессуары')]")
