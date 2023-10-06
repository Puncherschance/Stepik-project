from .base_page import BasePage
from pages.locators import MainPageLocators

class MainPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*MainPageLocators.BASKET_ADD), "Add to Basket button is not presented!"

    def open_basket_page(self):
        self.open_basket(*MainPageLocators.BASKET_ADD)

    def should_be_login_link(self):
        self.should_be_link(*MainPageLocators.LOGIN_LINK)

    def go_to_login_page(self):
        self.go_to_page(*MainPageLocators.LOGIN_LINK)


