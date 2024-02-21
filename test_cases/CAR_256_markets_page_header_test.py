import os

# import allure
import pytest
from playwright.sync_api import expect


@pytest.mark.usefixtures("setup")
class TestPageHeader:

    # @allure.title("Check the markets page header/logo and available tabs - C35686")
    @pytest.mark.test11
    def test_tab_header(self, login_to_app, markets_page, login_page):
        expect(markets_page.page_logo).to_be_visible()
        expect(markets_page.page_title).to_be_visible()
        expect(markets_page.overview_tab_locator).to_have_attribute("aria-selected", "true")
        expected_url = os.environ["URL"] + "/dashboard/market-sizing/overview"
        expect(markets_page.page).to_have_url(expected_url)

        markets_page.open_sales_tab()
        expect(markets_page.sales_tab_locator).to_have_attribute("aria-selected", "true")
        expected_url = os.environ["URL"] + "/dashboard/market-sizing/sales"
        expect(markets_page.page).to_have_url(expected_url)

        markets_page.open_pipeline_tab()
        expect(markets_page.pipeline_tab_locator).to_have_attribute("aria-selected", "true")
        expected_url = os.environ["URL"] + "/dashboard/market-sizing/pipeline"
        expect(markets_page.page).to_have_url(expected_url)

        markets_page.open_company_tab()
        expect(markets_page.company_tab_locator).to_have_attribute("aria-selected", "true")
        expected_url = os.environ["URL"] + "/dashboard/market-sizing/company"
        expect(markets_page.page).to_have_url(expected_url)
