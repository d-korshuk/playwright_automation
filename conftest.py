import pytest
from playwright.sync_api import sync_playwright
import requests
from pages.markets_page import MarketsPage
from pages.login_page import LoginPage
from playwright.sync_api import expect

import os

expect.set_options(timeout=15_000)

URL = os.environ['URL']
EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']
API_URL = os.environ['API_URL']
API_TOKEN = os.environ['API_TOKEN']


@pytest.fixture(scope="class")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="class")
def login_page(page):
    return LoginPage(page)


@pytest.fixture(scope="class")
def page(browser):
    return browser.new_page()


@pytest.fixture(scope="function")
def setup(browser, page):
    url = os.environ['URL']
    page.goto(url)


@pytest.fixture(scope="function")
def login_to_app(login_page):
    login_page.click_header_login_btn()
    email = os.environ['EMAIL']
    login_page.enter_email(email)
    login_page.click_next_btn()
    password = os.environ['PASSWORD']
    login_page.enter_password(password)
    login_page.click_submit_button()
    login_page.click_continue_wo_pass()
    yield


@pytest.fixture(scope="function")
def markets_page(page):
    return MarketsPage(page)

@pytest.fixture
def api_client():
    def _api_client(method, data, headers=None):
        if headers is None:
            headers = {}

        # Add default Authorization header
        headers["Authorization"] = f"Bearer {API_TOKEN}"

        url = API_URL

        if method.upper() == "GET":
            response = requests.get(url, params=data, headers=headers)
        elif method.upper() == "POST":
            response = requests.post(url, json=data, headers=headers)
        else:
            raise ValueError("Unsupported HTTP method")

        return response

    return _api_client
