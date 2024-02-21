import os

import pytest
#import allure
from playwright.sync_api import expect



@pytest.mark.usefixtures("setup")
class TestLoginPage:

    #@pytest.mark.login
    #@allure.title("Check the SSO flow for the registered user - C6952 ")
    def test_sso_login(self, login_page, dashboard_page, page):
        login_page.click_header_login_btn()
        email = os.environ['EMAIL']


        login_page.enter_email(email)
        login_page.click_next_btn()
        password = os.environ['PASSWORD']

        login_page.enter_password(password)
        login_page.click_submit_button()

        expect(dashboard_page.logout_btn_locator).to_be_visible()

    #@allure.title("Check that user in not able to login with invalid credentials - C6952 ")
    #@pytest.mark.login
    def test_sso_wrong_password(self, login_page, page):
        login_page.click_header_login_btn()
        email = os.environ['EMAIL']
        login_page.enter_email(email)
        login_page.click_next_btn()
        login_page.enter_password('Test123')
        login_page.click_submit_button()
        url_substring = "overview"

        expect(page).not_to_have_url(url_substring)
        expect(login_page.error_message_locator).to_be_visible()
