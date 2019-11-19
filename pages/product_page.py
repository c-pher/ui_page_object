from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

    # link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019'

    def add_book_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()
        self.solve_quiz_and_get_code()

    def should_be_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
               self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_MESSAGE).text, 'Product name does not equal'

    def should_be_right_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in \
               self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_MESSAGE_PRICE).text, 'Invalid price.'
