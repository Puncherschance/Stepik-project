from .base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "No such element!"
        assert self.element_text_is_correct(*BasketPageLocators.BASKET_EMPTY), "Basket is not empty!"





