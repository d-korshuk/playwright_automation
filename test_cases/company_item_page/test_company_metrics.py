import pytest
from playwright.sync_api import expect


@pytest.mark.usefixtures("setup")
class TestMCompanyMetrics:
    def test_company_metrics(self, login_to_app, company_page, api_client):

        data = {"context": "talaMarketDashboard",
                "request": {"functions": {"metrics_companyItem": {"years": [2023, 2029], "id": "1039"}}}}

        response = api_client("/item-page", "post", data=data)
        response_json = response.json()['response']['functions']['metrics_companyItem']['data'][0]

        expected_wwsales_2023 = response_json['worldwideSalesStart']
        if expected_wwsales_2023 is None:
            expected_wwsales_2023 = "No data"
        expected_wwsales_2029 = response_json['worldwideSalesEnd']
        if expected_wwsales_2029 is None:
            expected_wwsales_2029 = "No data"
        expected_wwsales_2029_diff = response_json['worldwideSalesDiff']
        expected_company_size = response_json['companySize']
        expected_cagr = response_json['CAGR']
        if expected_cagr is None:
            expected_cagr = "No data"
        expected_market_cap = response_json['marketCap']
        expected_drugs_sales_forecast = response_json['drugsSalesForecast']
        expected_profile = response_json['profile']
        expected_company_name = response_json['companyName']

        company_page.open_company_page()
        expect(company_page.logo_locator).to_be_visible()

        assert expected_company_name == company_page.company_name.inner_text()
        assert expected_company_size == company_page.company_size_locator.inner_text()
        assert expected_wwsales_2023 == company_page.wwsales_2023_locator.inner_text()
        assert expected_wwsales_2029 == company_page.wwsales_2029_locator.inner_text()
        assert expected_cagr == company_page.cagr_locator.inner_text()
        assert expected_market_cap == company_page.market_cap_locator.inner_text()
        assert expected_drugs_sales_forecast == company_page.drugs_sales_forecast.inner_text()

        company_page.show_more_locator.click()
        assert expected_profile in company_page.company_profile.inner_text()

        company_page.modal_close_locator.click()
        expect(company_page.modal_close_locator).not_to_be_visible()








