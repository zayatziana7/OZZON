from locators.mothers_children_locators import OzonMothersChildrenLocators as Mothers



class TestMothersChildren:

    def test_mothers_and_children(self, ozon_mothers_children):
        ozon_mothers_children.open_mothers_children()
        text = ozon_mothers_children.get_element_mothers_children_text(Mothers.MOTHERS_AND_CHILDREN)
        assert text == "Товары для мам и детей"


    def test_toys_and_games(self, ozon_mothers_children):
        ozon_mothers_children.open_mothers_children()
        ozon_mothers_children.click_to_tabs_mothers_children(Mothers.TOYS_AND_GAMES)
        text = ozon_mothers_children.get_element_mothers_children_text(Mothers.TOYS_AND_GAMES_VALUE)
        assert text == "Игрушки и игры"


    def test_children_food(self, ozon_mothers_children):
        ozon_mothers_children.open_mothers_children()
        ozon_mothers_children.click_to_tabs_mothers_children(Mothers.CHILDREN_FOOD)
        text = ozon_mothers_children.get_element_mothers_children_text(Mothers.CHILDREN_FOOD_VALUE)
        assert text == "Детское питание"


    def test_diapers_and_care(self, ozon_mothers_children):
        ozon_mothers_children.open_mothers_children()
        ozon_mothers_children.click_to_tabs_mothers_children(Mothers.DIAPETS_AND_CARE)
        text = ozon_mothers_children.get_element_mothers_children_text(Mothers.DIAPETS_AND_CARE_VALUE)
        assert text == "Детская гигиена и уход"


    def test_feeding_and_electronics(self, ozon_mothers_children):
        ozon_mothers_children.open_mothers_children()
        ozon_mothers_children.click_to_tabs_mothers_children(Mothers.FEEDING_AND_ELECTRONICS)
        text = ozon_mothers_children.get_element_mothers_children_text(Mothers.FEEDING_ELECTRONICS_VALUE)
        assert text == "Все товары по акции уже купили. Возможно, вам будут интересны другие предложения"


    def test_for_moms(self, ozon_mothers_children):
        ozon_mothers_children.open_mothers_children()
        ozon_mothers_children.click_to_tabs_mothers_children(Mothers.FOR_MOMS)
        text = ozon_mothers_children.get_element_mothers_children_text(Mothers.FOR_MOMS_VALUE)
        assert text == "Товары для мам"


    def test_clothes_and_accessories(self, ozon_mothers_children):
        ozon_mothers_children.open_mothers_children()
        ozon_mothers_children.click_to_tabs_mothers_children(Mothers.CLOTHES_ACCESSORIES)
        ozon_mothers_children.click_to_tabs_mothers_children(Mothers.CLOTHES_ACCESSORIES_C)
        text = ozon_mothers_children.get_element_mothers_children_text(Mothers.CLOTHES_ACCESSORIES_VALUE)
        assert text == 'Сумки, рюкзаки, аксессуары'
