# import allure
import pytest
from playwright.sync_api import expect

data = {"context": "talaMarketDashboard", "request": {"functions": {"metrics_overview": {"years": [2023, 2029]}}}}


@pytest.mark.usefixtures("setup")
class TestMetrics:

    def test_overview_tab_metrics(self, login_to_app, markets_page, api_client):
        response = api_client("post", data=data)
        response_json = response.json()['response']['functions']['metrics_overview']['data'][0]

        expected_overview_wwsales_2023 = response_json['worldwideSalesStart']
        expected_overview_wwsales_2029 = response_json['worldwideSalesEnd']
        if expected_overview_wwsales_2029 is None:
            expected_overview_wwsales_2029 = "No data"
        expected_overview_wwsales_2029_diff = response_json['worldwideSalesDiff']
        expected_overview_active_products = response_json['uniqueActiveProducts']
        expected_overview_act_companies = response_json['activeCompanies']
        expected_overview_top_company = response_json['topCompany']
        expected_overview_top_product = response_json['topProduct']

        assert expected_overview_wwsales_2023 == markets_page.overview_wwsales_2023_locator.inner_text()
        assert expected_overview_wwsales_2029 == markets_page.overview_wwsales_2029_locator.inner_text()
        assert str(expected_overview_wwsales_2029_diff) in markets_page.overview_wwsales_2029_diff_locator.inner_text()
        assert expected_overview_active_products == markets_page.overview_unique_act_products_locator.inner_text()
        assert expected_overview_act_companies == markets_page.overview_active_companies_locator.inner_text()
        assert expected_overview_top_company == markets_page.overview_top_company_locator.inner_text()
        assert expected_overview_top_product == markets_page.overview_top_product_locator.inner_text()

    def test_sales_tab_metrics(self, markets_page):
        markets_page.click_here_to_nav_to_dashboard()
        markets_page.open_sales_tab()
        expect(markets_page.sales_wwsales_2023_locator).to_have_text("$944m")
        expect(markets_page.sales_wwsales_2029_locator).to_have_text("$1,327m")
        expect(markets_page.sales_cagr_locator).to_have_text("+5.8%")
        expect(markets_page.sales_wwsales_2029_diff_locator).to_have_text("+383m")

    def test_pipeline_tab_metrics(self, markets_page):
        markets_page.click_here_to_nav_to_dashboard()
        markets_page.open_pipeline_tab()
        expect(markets_page.pipeline_products_locator).to_have_text("51,369")
        expect(markets_page.pipeline_products_by_indication_locator).to_have_text("51,512")
        expect(markets_page.pipeline_companies_locator).to_have_text("10,689")
        expect(markets_page.pipeline_indications_locator).to_have_text("844")

    def test_company_tab_metrics(self, markets_page):
        markets_page.click_here_to_nav_to_dashboard()
        markets_page.open_company_tab()
        expect(markets_page.company_active_companies_locator).to_have_text("717")
        expect(markets_page.company_wwsales_2023_locator).to_have_text("$944m")
        expect(markets_page.company_wwsales_2029_locator).to_have_text("$1,327m")
        expect(markets_page.company_wwsales_2029_diff_locator).to_have_text("+383m")
        expect(markets_page.company_cagr_locator).to_have_text("+5.8%")
        expect(markets_page.company_listed_locator).to_have_text("5338")
        expect(markets_page.company_private_locattor).to_have_text("403")
        expect(markets_page.company_pjv_locator).to_have_text("6")
