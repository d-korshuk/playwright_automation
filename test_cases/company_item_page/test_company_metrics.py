import pytest
from playwright.sync_api import expect


@pytest.mark.usefixtures("setup")
class TestMCompanyMetrics:
    def test_company_metrics(self, login_to_app, company_page):
        company_page.open_company_page()
        expect(company_page.logo_locator).to_be_visible()
