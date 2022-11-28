from selenium.webdriver.common.by import By


class OzonSezonLocators:
    VEGETABLES_FRUITS = (By.XPATH, "//a[contains(text(), ' Овощи, фрукты, зелень')]")
    VEGETABLES_FRUITS_VALUE = (By.XPATH, "//span[contains(text(), 'Мандарины Турция, 1 кг')]")
    TANGERINES = (By.XPATH, "//span[contains(text(), 'Мандарины Турция, 1 кг')]")
    TANGERINES_VALUE = (By.XPATH, "//h1[contains(text(), 'Мандарины Турция, 1 кг')]")
    QUINCE = (By.XPATH, "//span[contains(text(), 'Айва, ароматная, множество витаминов, Узбекистан, 2 шт')]")
    QUINCE_VALUE = (By.XPATH, "//h1[contains(text(), 'Айва, ароматная, множество витаминов, Узбекистан, 2 шт')]")
    POMEGRANATE = (By.XPATH, "//span[contains(text(), 'Гранат отборный, новый урожай, 1 шт')]")
    POMEGRANATE_VALUE = (By.XPATH, "//h1[contains(text(), 'Гранат отборный, новый урожай, 1 шт')]")
    TANGERINES_MINI = (By.XPATH, "//span[contains(text(), 'Мандарины мини с зеленцой, 500 г')]")
    TANGERINES_MINI_VALUE = (By.XPATH, "//h1[contains(text(), 'Мандарины мини с зеленцой, 500 г')]")
    GRAPE = (By.XPATH, "//span[contains(text(), 'Виноград Киш-Миш, без косточек, 500 г')]")
    GRAPE_VALUE = (By.XPATH, "//h1[contains(text(), 'Виноград Киш-Миш, без косточек, 500 г')]")
    PERSIMMON_KOROLEK = (By.XPATH, "//span[contains(text(), 'Хурма Королек, осенняя, с зелеными бочками, 1 кг')]")
    PERSIMMON_KOROLEK_VALUE = (By.XPATH, "//h1[contains(text(), 'Хурма Королек, осенняя, с зелеными бочками, 1 кг')]")
    PINEAPPLE = (By.XPATH, "//span[contains(text(), 'Ананас, 1 шт')]")
    PINEAPPLE_VALUE = (By.XPATH, "//h1[contains(text(), 'Ананас, 1 шт')]")
    WATERMEION_MINI = (By.XPATH, "//span[contains(text(), 'Арбуз мини красный, с мягкими косточками, 1 шт')]")
    WATERMEION_MINI_VALUE = (By.XPATH, "//h1[contains(text(), 'Арбуз мини красный, с мягкими косточками, 1 шт')]")
    GRANBERRY = (By.XPATH, "//span[contains(text(), 'Клюква свежая, витаминная, 250 г')]")
    GRANBERRY_VALUE = (By.XPATH, "//h1[contains(text(), 'Клюква свежая, витаминная, 250 г')]")
    ASPARAGUS = (By.XPATH, "//span[contains(text(), 'Спаржа зеленая Artfruit, 250 г')]")
    ASPARAGUS_VALUE = (By.XPATH, "//h1[contains(text(), 'Спаржа зеленая Artfruit, 250 г')]")
    QUESTION_ASPARAGUS = (By.XPATH, "//div[contains(text(), 'Задать вопрос')]")
    QUESTION_ASPARAGUS_VALUE = (By.XPATH, "//div[contains(text(), 'Задайте вопрос о товаре')]")
    REVIEWS = (By.CSS_SELECTOR, 'a[href^="/product/sparzha-zelenaya-artfruit-250-g-387081227/reviews/"]')
    REVIEWS_VALUE = (By.XPATH, "//a[contains(text(), 'Отзывы')]")
    OPIS = (By.CSS_SELECTOR, 'a[href^="#section-description--offset-140"]')
    TT = (By.XPATH, "//a[contains(text(), 'Характеристики')]")
    VIDEO = (By.CSS_SELECTOR, 'a[href^="https://www.ozon.ru/product/mandariny-turtsiya-1-kg-202923460/videos/"]')
    VIDEO_VALUE = (By.XPATH, "//h1[contains(text(), 'Фото и видео пользователей')]")
    DELIVERY = (By.CSS_SELECTOR, 'a[href^="/my/deliveryPriceInfo"]')
    DELIVERY_VALUE = (By.XPATH, "//title[contains(text(), 'Стоимость доставки')]")
    PAYMENT = (By.CSS_SELECTOR, 'a[href^="https://docs.ozon.ru/common/oplata/sposoby-oplaty"]')
    PAYMENT_VALUE = (By.ID, 'pageTitle')
    COLLECTIONS = (By.XPATH, "//h2[contains(text(), 'Подборки товаров в категории Цитрусовые')]")
    POMELO = (By.CSS_SELECTOR, 'a[href^="/category/pomelo-so-skidkoy/"]')
    POMELO_VALUE = (By.XPATH, "//div[contains(text(), 'Товары не в наличии')]")
    QUESTIOS = (By.XPATH, "//span[contains(text(), 'Вопросы и ответы о товаре')]")
    QUESTIOS_VALUE = (By.XPATH, "//div[contains(text(), 'Задайте вопрос о товаре')]")
    Y = (By.XPATH, "//span[contains(text(), 'Написать отзыв')]")
    Y_Y = (By.XPATH, "//div[contains(text(), 'Введите номер телефона')]")
    E = (By.XPATH, "//span[contains(text(), 'Узнать о снижении цены')]/../..")
    E_E = (By.XPATH, "//h1[contains(text(), 'Уточнение адреса')]")
    OO = (By.XPATH, "//span[contains(text(), 'Добавить в корзину')]/../..")
    O_OO = (By.XPATH, "//span[contains(text(), 'Уточнение адреса')]")
    PP = (By.XPATH, "//div[contains(text(), 'Задать вопрос')]")
    DELIVERY_TERMS = (By.CSS_SELECTOR, 'a[href^="/my/deliveryPriceInfo"]')
    DELIVERY_TERMS_VALUE =(By.XPATH, "//div[contains(text(), 'Стоимость доставки')]")
    RETURN_OF_DOODS = (By.CSS_SELECTOR, 'a[href^="https://docs.ozon.ru/common/otmena-i-vozvrat-zakaza/kak-vernut-tovar"]')
    RETURN_OF_DOODS_VALUE = (By.ID, 'pageTitle')
    REFUND = (By.CSS_SELECTOR, 'a[href^="https://docs.ozon.ru/common/otmena-i-vozvrat-zakaza/vozvrat-deneg-i-ballov/"]')
    REFUND_VALUE = (By.ID, 'pageTitle')
    MOSCOW = (By.XPATH, "//span[contains(text(), 'Москва')]/../..")
    MOSCOW_VALUE = (By.XPATH, "//span[contains(text(), 'Куда доставить заказ?')]")
    PICK_UP_POINTS = (By.XPATH, "//span[contains(text(), 'Пункты выдачи и постаматы')]/../..")
    PICK_UP_POINTS_VALUE = (By.XPATH, "//h1[contains(text(), ' Москва - пункты выдачи заказов OZON')]")
    QQ = (By.XPATH, "//span[contains(text(), 'Узнать о снижении цены')]/../..")
    QQ_W = (By.XPATH, "//h1[contains(text(), 'Узнайте о снижении цены')]")
    II = (By.XPATH, "//span[contains(text(), 'Написать отзыв')]/../..")
    II_I = (By.XPATH, "//div[contains(text(), 'Введите номер телефона')]")
