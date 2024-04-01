import pytest
from playwright.sync_api import sync_playwright
import requests

from pages.company_item_page import CompanyItemPage
from pages.markets_page import MarketsPage
from pages.login_page import LoginPage
from playwright.sync_api import expect

import os
from dotenv import load_dotenv
load_dotenv()

expect.set_options(timeout=15_000)

URL = os.environ.get("URL")
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
API_URL = os.environ.get("API_URL")
API_TOKEN_URL = os.environ.get("API_TOKEN_URL")
CLIENT_ID = os.environ.get("CLIENT_ID")
AUDIENCE = os.environ.get("AUDIENCE")


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
def company_page(page):
    return CompanyItemPage(page)


@pytest.fixture(scope="class")
def page(browser):
    return browser.new_page()


@pytest.fixture(scope="function")
def setup(browser, page):
    url = os.environ['URL']
    page.goto(url)
    configure_browser_context(page.context)


def configure_browser_context(context):
    context.grant_permissions(["clipboard-read", "notifications", "clipboard-write"])


@pytest.fixture(scope="function")
def login_to_app(login_page):
    login_page.click_header_login_btn()
    email = os.environ.get('EMAIL')
    login_page.enter_email(email)
    login_page.click_next_btn()
    password = os.environ.get('PASSWORD')
    login_page.enter_password(password)
    login_page.click_submit_button()
    login_page.click_continue_wo_pass()
    yield


@pytest.fixture(scope="function")
def markets_page(page):
    return MarketsPage(page)


@pytest.fixture
def api_client():
    def _api_client(endpoint, method, data, headers=None):
        if headers is None:
            headers = {}
        api_token = get_api_token()

        headers["Authorization"] = f"Bearer {api_token}"
        url = API_URL + endpoint

        if method.upper() == "GET":
            response = requests.get(url, params=data, headers=headers)
        elif method.upper() == "POST":
            response = requests.post(url, json=data, headers=headers)
        else:
            raise ValueError("Unsupported HTTP method")

        return response

    return _api_client


def get_api_token():
    url = API_TOKEN_URL
    payload = {
        "username": EMAIL,
        "password": PASSWORD,
        "client_id": CLIENT_ID,
        "audience": AUDIENCE,
        "grant_type": "password"
    }
    response = requests.post(url, json=payload)
    return response.json().get("access_token")
