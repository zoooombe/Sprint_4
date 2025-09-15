import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='function')
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')

    options.set_capability('acceptInsecureCerts', True)
    options.set_capability('unhandledPromptBehavior', 'ignore')

    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()),
        options=options
    )

    driver.set_page_load_timeout(30)
    driver.implicitly_wait(10)

    yield driver

    try:
        driver.quit()
    except:
        pass