from selenium import webdriver
import pytest
from colorama import Fore
import time
from selenium.webdriver.chrome.options import Options as OptionsChrome
# from selenium.webdriver.common.by import By
# from selenium_stealth import stealth

def pytest_addoption(parser):
    parser.addoption("--language", action = "store", default = None, help = "Choose language!")

@pytest.fixture()
def browser(request):

    user_language = request.config.getoption("language") #  поддерживается только для Chrome
    chrome_options = OptionsChrome()
    print('\n', Fore.YELLOW + "\nStarting Chrome browser for tests.")
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})  # не работает без использования stealth-модуля
    browser = webdriver.Chrome()(options = chrome_options)
    #stealth(browser, languages=[user_language, "es"], platform="Win32")  # As of now selenium-stealth only support Selenium Chrome.
    browser.maximize_window()
    print("Begin Test Case.")
    yield browser
    time.sleep(2)
    print("\nQuit browser.")
    browser.quit()


