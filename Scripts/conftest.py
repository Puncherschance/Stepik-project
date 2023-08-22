from selenium import webdriver
import pytest
from colorama import Fore
import time
from selenium.webdriver.chrome.options import Options as OptionsChrome


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default=None, help="Choose language!")


@pytest.fixture()
def browser(request):

    user_language = request.config.getoption("language")
    chrome_options = OptionsChrome()
    print('\n', Fore.YELLOW + "\nStarting Chrome browser for tests.")
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    print("Begin Test Case.")
    yield browser
    time.sleep(2)
    print("\nQuit browser.")
    browser.quit()
