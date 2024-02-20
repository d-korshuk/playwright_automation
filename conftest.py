import configparser
import pytest
from playwright.sync_api import sync_playwright

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from playwright.sync_api import expect

expect.set_options(timeout=15_000)


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def login_page(page):
    return LoginPage(page)


@pytest.fixture(scope="function")
def config():
    parser = configparser.ConfigParser()
    parser.read("config/credentials.ini")
    return parser


@pytest.fixture(scope="function")
def page(browser):
    return browser.new_page()


@pytest.fixture(scope="function")
def setup(browser, page, config):
    url = config.get('app', 'url')
    page.goto(url)


@pytest.fixture(scope="function")
def login_to_app(login_page, config):
    login_page.click_header_login_btn()
    email = config.get('app', 'brand_email')
    login_page.enter_email(email)
    login_page.click_next_btn()
    password = config.get('app', 'password')
    login_page.enter_password(password)
    login_page.click_submit_button()
    yield


@pytest.fixture(scope="function")
def dashboard_page(page):
    return DashboardPage(page)
