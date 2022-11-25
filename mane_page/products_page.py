from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from locators.ozon_fresh_locators import OzonFreshPageLocators as Ozon





class OzonProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_presence_of_element_located(self, locator: tuple,
                                         timeout=10) -> WebElement:
        """
        Wait presence of an element located and return this element
        :param locator: element's locator
        :type locator: tuple
        :param timeout: time to wait for an element
        :type timeout: int
        :return: WebElement
        """
        return WebDriverWait(self.driver, timeout=timeout) \
            .until(ec.presence_of_element_located(locator),
                   message=f'Element with locator {locator[1]} is not presented')

    def find_element_and_click(self, locator: tuple):
        """
        Method to find element and click on it
        :param locator:
        :return: BasePage instance
        """
        self.wait_element_to_be_clickable(locator).click()
        return self

    def find_element_and_click_via_script(self, locator: tuple):
        """
        Method to find element and click on it via JS script
        :param locator:
        :return: BasePage instance
        """
        self.driver.execute_script("arguments[0].click();", self.wait_presence_of_element_located(locator))
        return self

    def find_element_and_click_via_action_chains(self, locator: tuple):
        """
        Method to scroll to an element
        :param locator:
        :return: BasePage instance
        """
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        return self

    def wait_element_to_be_clickable(self, locator: tuple, timeout=10) -> WebElement:
        """
        Wait element to be clickable and return this element
        :param locator: element's locator
        :type locator: tuple
        :param timeout: time to wait for an element
        :type timeout: int
        :return: WebElement instance
        """
        return WebDriverWait(self.driver, timeout=timeout) \
            .until(ec.element_to_be_clickable(locator),
                   message=f'Element with locator {locator[1]} is not clickable!')

    def click_to_tabs_products(self, locator):
        self.find_element_and_click_via_script(locator)

    def get_element_products_text(self, locator):
        element = self.wait_presence_of_element_located(locator)
        return element.text

    def open_products(self):
        self.click_to_tabs_products(Ozon.OZON_FRESH)
        self.click_to_tabs_products(Ozon.PRODUCTS)