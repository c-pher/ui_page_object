from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_MAIL = (By.NAME, 'registration-email')
    REGISTER_PASSWORD = (By.NAME, 'registration-password1')
    REGISTER_PASSWORD_CONFIRM = (By.NAME, 'registration-password2')
    REGISTER = (By.NAME, 'registration_submit')


class ProductPageLocators:
    ADD_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    ADDED_PRODUCT_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1) > .alertinner strong')
    ADDED_PRODUCT_MESSAGE_PRICE = (By.CSS_SELECTOR, '#messages div:nth-child(3) > .alertinner strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group > a')
    USER_ICON = (By.CLASS_NAME, 'icon-user')


class BasketPageLocators:
    BASKET_MESSAGE_EMPTY = (By.CLASS_NAME, 'content')
    BASKET_TITLE = (By.CLASS_NAME, 'basket-title')
