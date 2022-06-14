from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    text_empty_basket = 'Ваша корзина пуста'

    def should_be_basket_url(self):
        assert self.browser.current_url, "Basket url is not presented"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_TEXT)

    def should_not_be_product_information(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT_INFORMATION), \
            "Product information is presented, but should not be"