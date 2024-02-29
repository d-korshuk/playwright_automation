from playwright.sync_api import Page


class CompanyItemPage:
    def __init__(self, page=Page):
        self.page = page

        # Top panel locators
        self.logo_locator = page.get_by_test_id("DomainIcon").first
        self.company_size_locator = page.get_by_test_id("companySize")
        self.wwsales_2022_locator = page.get_by_test_id("worldwideSalesStart")
        self.wwsales_2028_locator = page.get_by_test_id("worldwideSalesEnd")
        self.wwsales_2028_diff_locator = page.get_by_test_id("worldwideSalesDiff")
        self.cagr_locator = page.get_by_test_id("cagr")
        self.market_cap_locator = page.get_by_test_id("marketCap")
        self.drugs_sales_forecast = page.get_by_test_id("drugsSalesForecast")



