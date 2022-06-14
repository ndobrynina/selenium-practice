from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    product_name = ''
    product_price = ''
    product_description = ''

    def should_be_product_url(self):
        assert self.browser.current_url, "Product url is not presented"

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add button is not presented"

    def click_on_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def should_be_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Name of product not found"
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Price of product not found"
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_description(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION), "Description of product not found"
        self.product_description = self.browser.find_element(*ProductPageLocators.PRODUCT_DESCRIPTION).text

    def should_be_success(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Message of Success added product in " \
                                                                               "basket not found "

    def check_success_message(self):
        msg_lst = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES)
        assert len(msg_lst) == 3, "Success message not found"

        assert self.product_name == msg_lst[0].text, "Wrong name product added to basket"
        assert self.product_price == msg_lst[2].text, "Wrong price product added to basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), \
            "Success message is disappeared, but should not be"