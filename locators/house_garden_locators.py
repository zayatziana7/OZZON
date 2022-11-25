from selenium.webdriver.common.by import By


class OzonHouseGardenLocators:
    HOUSEGARDEN = (By.CSS_SELECTOR, 'a[href^="/category/dom-i-sad-14500/"]')
    HOUSEGARDEN_VALUE= (By.XPATH, "//h1[contains(text(), 'Дом и сад')]")
    FLOWERS_DELIVERY =(By.CSS_SELECTOR, 'a[href^="/category/bukety-35944/"]')
    FLOWERS_DELIVERY_VALUE = (By.XPATH, "//h1[contains(text(), 'Букеты цветов')]")