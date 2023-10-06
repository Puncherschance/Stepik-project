from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_ADD = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs a")

class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    #LOGIN_FORM_EMAIL =  (By.CSS_SELECTOR, "input[name='login-username']")
    #LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "input[name='login-password']")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REGISTER_FORM_REPEAT_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    BASKET_ADD = (By.CSS_SELECTOR, "#add_to_basket_form button")
    BASKET_ITEM = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    BASKET_TOTAl = (By.CSS_SELECTOR, "#messages  p:nth-child(1) strong")
    BOOK_NAME = (By.CSS_SELECTOR, "#content_inner h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "#content_inner p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) div")
    BASKET_VIEW = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs a")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
