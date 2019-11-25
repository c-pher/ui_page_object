import time

import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage


@pytest.mark.need_review
@pytest.mark.parametrize('n', [
    0, 1, 2, 3, 4, 5, 6,
    pytest.param(7, marks=pytest.mark.xfail),
    8, 9
])
def test_guest_can_add_product_to_basket(browser, n):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{str(n)}'
    page = ProductPage(browser, link)
    page.open()
    page.add_book_to_basket()
    page.should_be_in_basket()
    page.should_be_right_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPage.link)
    page.open()
    page.add_book_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPage.link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPage.link)
    page.open()
    page.add_book_to_basket()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    Гость открывает страницу товара
    Переходит в корзину по кнопке в шапке
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста
    """

    page = MainPage(browser, MainPage.link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, BasketPage.link)
    basket_page.should_be_empty()
    basket_page.should_not_be_products()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, LoginPage.link)
        page.open()
        email = str(time.time()) + '@fakemail.org'
        page.register_new_user(email, '!23456789@')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, ProductPage.link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, ProductPage.link)
        page.open()
        page.add_book_to_basket()
        page.should_be_in_basket()
        page.should_be_right_price()
