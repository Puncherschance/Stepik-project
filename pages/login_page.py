from .base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"\nExpected 'login' in {self.browser.current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not presented!"
        #assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_EMAIL), "email field is not presented"
        #assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_PASSWORD), "password field is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "registration form is not presented!"
        #assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_EMAIL), "email field is not presented"
        #assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_PASSWORD), "password field is not presented"
        #assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_REPEAT_PASSWORD), "repeat_password field is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_REPEAT_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT).click()

