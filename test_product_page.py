from pages.product_page import ProductPage


def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser, ProductPage.link)
    page.open()
    page.add_book_to_basket()
    page.should_be_in_basket()
    page.should_be_right_price()
