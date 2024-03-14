import pytest
from playwright.sync_api import expect


@pytest.mark.usefixtures("setup")
class TestWidget:

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




