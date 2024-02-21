#import allure
import pytest
from playwright.sync_api import expect


@pytest.mark.usefixtures("setup")
class TestWidget:

    #@pytest.mark.widget
    #@allure.title("Check the expanding of widget - 39710")
    #def test_expand_widget(self, login_to_app, markets_page):
    #    markets_page.open_overview_tab()
    #    markets_page.expand_widget()
     #   expect(markets_page.wwsales_2022_locator).not_to_be_visible()

    #@pytest.mark.widget1
    #@allure.title("Check switching between tabs - C39772")
    def test_switch_tabs(self, login_to_app, markets_page):
        markets_page.open_overview_tab()

        markets_page.select_companies_tab()

        expect(markets_page.top_by_sales_companies_tab_locator).to_have_attribute("aria-pressed", "true")

        markets_page.select_technology_tab()
        expect(markets_page.top_by_sales_technology_tab_locator).to_have_attribute("aria-pressed", "true")

        markets_page.select_moa_tab()
        expect(markets_page.top_by_sales_moa_tab_locator).to_have_attribute("aria-pressed", "true")

        markets_page.select_product_tab()
        expect(markets_page.top_by_sales_product_tab_locator).to_have_attribute("aria-pressed", "true")




