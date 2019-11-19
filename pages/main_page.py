from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    link = 'http://selenium1py.pythonanywhere.com/'

    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'Login link is not presented'
