import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    Гость открывает главную страницу
    Переходит в корзину по кнопке в шапке сайта
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста
    """

    page = MainPage(browser, MainPage.link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, BasketPage.link)
    basket_page.should_be_empty()
    basket_page.should_not_be_products()


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, MainPage.link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, MainPage.link)
        page.open()
        page.should_be_login_link()
