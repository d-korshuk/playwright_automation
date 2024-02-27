# import allure
import pytest
from playwright.sync_api import expect


@pytest.mark.usefixtures("setup")
class TestOverviewMetrics:

    def test_overview_tab_metrics(self, login_to_app, markets_page):
        expect(markets_page.overview_wwsales_2022_locator).to_have_text("$944m")
        expect(markets_page.overview_wwsales_2028_locator).to_have_text("$1,327m")
        expect(markets_page.overview_wwsales_2028_diff_locator).to_have_text("+383m")
        expect(markets_page.overview_unique_act_products_locator).to_have_text("4,632")
        expect(markets_page.overview_active_companies_locator).to_have_text("717")
        expect(markets_page.overview_top_company_locator).to_have_text("Pfizer")
        expect(markets_page.overview_top_product_locator).to_have_text("Comirnaty")
