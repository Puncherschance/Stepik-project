from .base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"\nExpected 'login' in {self.browser.current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login is not presented"
        #assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_EMAIL), "email field is not presented"
        #assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_PASSWORD), "password field is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "registration is not presented"
        #assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_EMAIL), "email field is not presented"
        #assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_PASSWORD), "password field is not presented"
        #assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_REPEAT_PASSWORD), "repeat_password field is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()