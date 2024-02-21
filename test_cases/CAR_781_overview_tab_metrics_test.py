# import allure
import pytest
from playwright.sync_api import expect


@pytest.mark.usefixtures("setup")
class TestOverviewMetrics:

    @pytest.mark.test44
    def test_overview_tab_metrics(self, login_to_app, markets_page):
        expect(markets_page.wwsales_2022_locator).to_have_text("$944m")
        expect(markets_page.wwsales_2028_locator).to_have_text("$1,320m")
        expect(markets_page.wwsales_2028_diff_locator).to_have_text("+376m")
        expect(markets_page.unique_act_products_locator).to_have_text("4,612")
        expect(markets_page.active_companies_locator).to_have_text("714")
        expect(markets_page.top_company_locator).to_have_text("Pfizer")
        expect(markets_page.top_product_locator).to_have_text("Comirnaty")
