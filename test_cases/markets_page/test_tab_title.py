#import allure
import pytest
from playwright.sync_api import expect


@pytest.mark.usefixtures("setup")
class TestPageTitle:


    #@allure.title("Check the tab title - C7294")
    def test_tab_title(self, login_to_app, markets_page):
        expected_title = "Evaluate"
        expect(markets_page.page).to_have_title(expected_title)
