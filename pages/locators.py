from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, 'login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    ADDED_PRODUCT_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1) > .alertinner')
    ADDED_PRODUCT_MESSAGE_PRICE = (By.CSS_SELECTOR, '#messages div:nth-child(3) > .alertinner strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
