import os
from playwright.sync_api import Page


class CompanyItemPage:
    def __init__(self, page=Page):
        self.page = page

        # Top panel locators
        self.logo_locator = page.get_by_test_id("DomainIcon").first
        self.company_name = page.get_by_role("heading", name="Johnson & Johnson")
        self.company_profile = page.get_by_label("Johnson & Johnson").locator("div").first
        self.company_size_locator = page.get_by_test_id("companySize")
        self.wwsales_2023_locator = page.get_by_test_id("noMetricsData").first
        self.wwsales_2029_locator = page.get_by_test_id("noMetricsData").nth(1)
        self.wwsales_2029_diff_locator = page.get_by_test_id("worldwideSalesDiff")
        self.cagr_locator = page.get_by_test_id("noMetricsData").nth(2)
        self.market_cap_locator = page.get_by_test_id("marketCap")
        self.drugs_sales_forecast = page.get_by_test_id("drugsSalesForecast")
        self.show_more_locator = page.get_by_text("Show more")
        self.modal_close_locator = page.get_by_label("close")

    def open_company_page(self):
        url = os.environ.get("URL") + "/dashboard/company/1039"
        self.page.goto(url)



