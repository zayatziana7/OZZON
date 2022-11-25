from selenium.webdriver.common.by import By


class OzonDairyLocators:
    VEGETABLE_EGGS = (By.XPATH, "//span[contains(text(), 'Яйца куриные Ozon fresh, С1, 10 шт')]")
    VEGETABLE_EGGS_VALUE = (By.XPATH, "//h1[contains(text(), 'Яйца куриные Ozon fresh, С1, 10 шт')]")
    CHICKEN_EGGS = (By.XPATH, "//span[contains(text(), 'Яйца куриные Ozon fresh, С2, 10 шт')]")
    CHICKEN_EGGS_VALUE = (By.XPATH, "//h1[contains(text(), 'Яйца куриные Ozon fresh, С2, 10 шт')]")
    SELECTED_EGGS = (By.XPATH, "//span[contains(text(), 'Яйца куриные Ozon fresh, отборные СО, 10 шт')]")
    SELECTED_EGGS_VALUE = (By.XPATH, "//h1[contains(text(), 'Яйца куриные Ozon fresh, отборные СО, 10 шт')]")
