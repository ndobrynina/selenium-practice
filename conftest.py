import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language == "en":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    else:
        raise pytest.UsageError("--language should be not None")
    yield browser
    print("\nquit browser..")
    browser.quit()