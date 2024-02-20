import configparser
import pytest
from playwright.sync_api import sync_playwright

import config.secret_config
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from playwright.sync_api import expect

import os

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
def page(browser):
    return browser.new_page()


@pytest.fixture(scope="function")
def setup(browser, page):
    url = config.secret_config.URL
    page.goto(url)


@pytest.fixture(scope="function")
def login_to_app(login_page):
    login_page.click_header_login_btn()
    email = config.secret_config.EMAIL
    login_page.enter_email(email)
    login_page.click_next_btn()
    password = config.secret_config.PASSWORD
    login_page.enter_password(password)
    login_page.click_submit_button()
    yield


@pytest.fixture(scope="function")
def dashboard_page(page):
    return DashboardPage(page)
