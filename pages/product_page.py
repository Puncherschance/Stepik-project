from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_ADD), "Add to Basket button is not presented!"

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_VIEW), "Basket button is not presented!"

    def open_basket_page(self):
        self.open_basket(*ProductPageLocators.BASKET_VIEW)

    def add_item_to_basket(self):
        basket_add = self.browser.find_element(*ProductPageLocators.BASKET_ADD)
        basket_add.click()
        #self.solve_quiz_and_get_code()
        #assert self.solve_quiz_and_get_code() == True, "Alert is not shown!"

    def basket_content_should_be_correct(self):
        basket_item = self.browser.find_element(*ProductPageLocators.BASKET_ITEM)
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAl)
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        assert basket_item.text == book_name.text, "Book name is incorrect!"
        assert basket_total.text == book_price.text, "Basket total is incorrect!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_not_be_success_message_by_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_login_link(self):
        self.should_be_link(*ProductPageLocators.LOGIN_LINK)

    def go_to_login_page(self):
        self.go_to_page(*ProductPageLocators.LOGIN_LINK)