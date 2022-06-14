from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SHOW_BASKET = (By.CSS_SELECTOR, ".btn-group > a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, 'input[name=registration-email]')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REPEAT_REGISTER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name=registration_submit]')
    SUCCESS_MESSAGE_REGISTRATION = (By.CSS_SELECTOR, ".alertinner wicon")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#product_description+p")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")

class BasketPageLocators:
    BASKET_TEXT = (By.CSS_SELECTOR, "div #content_inner > p")
    BASKET_PRODUCT_INFORMATION = (By.CSS_SELECTOR, ".basket-title >.row > h2")
