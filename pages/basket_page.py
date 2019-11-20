from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/basket/'

    def should_be_empty(self):
        assert 'empty' in self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE_EMPTY).text

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE)
