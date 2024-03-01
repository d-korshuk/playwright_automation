# import allure
import pytest
from playwright.sync_api import expect


@pytest.mark.usefixtures("setup")
class TestMetrics:

    def test_overview_tab_metrics(self, login_to_app, markets_page, api_client):
        data = {"context": "talaMarketDashboard",
                "request": {"functions": {"metrics_overview": {"years": [2023, 2029]}}}}

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

    def test_sales_tab_metrics(self, markets_page, api_client):
        data = {"context": "talaMarketDashboard",
                "request": {"functions": {"metrics_sales": {"years": [2023, 2029]}}}}

        response = api_client("post", data=data)
        response_json = response.json()['response']['functions']['metrics_sales']['data'][0]

        markets_page.click_here_to_nav_to_dashboard()
        markets_page.open_sales_tab()

        expected_sales_wwsales_2023 = response_json['worldwideSalesStart']
        expected_sales_wwsales_2029 = response_json['worldwideSalesEnd']
        if expected_sales_wwsales_2029 is None:
            expected_sales_wwsales_2029 = "No data"
        expected_sales_wwsales_2029_diff = response_json['worldwideSalesDiff']
        expected_sales_cagr = response_json['CAGR']
        if expected_sales_cagr is None:
            expected_sales_cagr = "No data"

        assert expected_sales_wwsales_2023 == markets_page.sales_wwsales_2023_locator.inner_text()
        assert expected_sales_wwsales_2029 == markets_page.sales_wwsales_2029_locator.inner_text()
        assert str(expected_sales_wwsales_2029_diff) in markets_page.sales_wwsales_2029_diff_locator.inner_text()
        assert expected_sales_cagr == markets_page.sales_cagr_locator.inner_text()

    def test_pipeline_tab_metrics(self, markets_page, api_client):
        data = {"context": "talaMarketDashboard",
                "request": {"functions": {"metrics_pipeline": {"years": {}}}}}

        response = api_client("post", data=data)
        response_json = response.json()['response']['functions']['metrics_pipeline']['data'][0]

        markets_page.click_here_to_nav_to_dashboard()
        markets_page.open_pipeline_tab()

        expected_pipeline_products = response_json['products']
        expected_pipeline_products_indications = response_json['productsIndication']
        expected_pipeline_companies = response_json['companies']
        expected_pipeline_indications = response_json['indications']

        assert expected_pipeline_products == markets_page.pipeline_products_locator.inner_text()
        assert expected_pipeline_products_indications == markets_page.pipeline_products_by_indication_locator.inner_text()
        assert expected_pipeline_companies == markets_page.pipeline_companies_locator.inner_text()
        assert expected_pipeline_indications == markets_page.pipeline_indications_locator.inner_text()

    def test_company_tab_metrics(self, markets_page, api_client):
        data = {"context":"talaMarketDashboard",
                "request":{"functions":{"metrics_company":{"years":[2023,2029]}}}}

        response = api_client("post", data=data)
        response_json = response.json()['response']['functions']['metrics_company']['data'][0]

        markets_page.click_here_to_nav_to_dashboard()
        markets_page.open_company_tab()

        expected_company_active_companies = response_json['activeCompanies']
        expected_company_ww_sales_2023 = response_json['worldwideSalesStart']
        expected_company_ww_sales_2029 = response_json['worldwideSalesEnd']
        if expected_company_ww_sales_2029 is None:
            expected_company_ww_sales_2029 = "No data"
        expected_company_ww_sales_diff = response_json['worldwideSalesDiff']
        expected_company_cagr = response_json['CAGR']
        if expected_company_cagr is None:
            expected_company_cagr = "No data"
        expected_company_listed = response_json['listedCompanies']
        expected_company_private = response_json['privateCompanies']
        expected_company_pjv = response_json['privateJVCompanies']

        assert expected_company_active_companies == markets_page.company_active_companies_locator.inner_text()
        assert expected_company_ww_sales_2023 == markets_page.company_wwsales_2023_locator.inner_text()
        assert expected_company_ww_sales_2029 == markets_page.company_wwsales_2029_locator.inner_text()
        assert str(expected_company_ww_sales_diff) in markets_page.company_wwsales_2029_diff_locator.inner_text()
        assert expected_company_cagr == markets_page.company_cagr_locator.inner_text()
        assert expected_company_listed == markets_page.company_listed_locator.inner_text()
        assert expected_company_private == markets_page.company_private_locator.inner_text()
        assert expected_company_pjv == markets_page.company_pjv_locator.inner_text()


