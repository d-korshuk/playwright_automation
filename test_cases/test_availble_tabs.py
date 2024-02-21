import time

#import allure
import pytest
from playwright.sync_api import expect


@pytest.mark.usefixtures("setup")
class TestTabs:

    #@pytest.mark.tabs
    #@allure.title("Check the tab title - C7294")
    def test_tab_title(self, login_to_app, dashboard_page, login_page):
        time.sleep(3)

        expect(dashboard_page.wwsales_2022_locator).to_be_visible()
        expect(dashboard_page.wwsales_2028_locator).to_be_visible()
        expect(dashboard_page.unique_act_products_locator).to_be_visible()
        expect(dashboard_page.active_companies_locator).to_be_visible()
        expect(dashboard_page.top_company_locator).to_be_visible()
        expect(dashboard_page.top_product_locator).to_be_visible()






