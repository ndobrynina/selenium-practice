from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SHOW_BASKET = (By.CSS_SELECTOR, ".btn-group > a.btn-default")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#product_description+p")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")

class BasketPageLocators:
    BASKET_TEXT = (By.CSS_SELECTOR, "div #content_inner > p")
    BASKET_PRODUCT_INFORMATION = (By.CSS_SELECTOR, ".basket-title >.row > h2")


class SingletonFive:
    count = 0
    __obj = None

    def __new__(cls, *args, **kwargs):
        if cls.count <= 5:
            cls.__obj = super().__new__(cls)
            cls.count += 1
        return cls.__obj

    def __init__(self, name):
        self.name = name

class SingletonFive:
    count = 0
    __obj = None

    def __new__(cls, *args, **kwargs):
        if cls.count < 5:
            cls.__obj = super().__new__(cls)
        cls.count += 1
        return cls.__obj

    def __init__(self, name):
        self.name = name