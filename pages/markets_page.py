from playwright.sync_api import Page


class MarketsPage:
    def __init__(self, page=Page):
        self.page = page
        self.overview_tab_locator = page.get_by_role("tab", name="overview")
        self.sales_tab_locator = page.get_by_role("tab", name="sales")
        self.pipeline_tab_locator = page.get_by_role("tab", name="pipeline")
        self.company_tab_locator = page.get_by_role("tab", name="company")
        self.logout_btn_locator = page.get_by_role("button", name="Logout")

        # Overview tab locators

        self.wwsales_2022_locator = page.get_by_test_id("worldwideSalesStart")
        self.wwsales_2028_locator = page.get_by_test_id("worldwideSalesEnd")
        self.wwsales_2028_diff_locator = page.get_by_test_id("worldwideSalesDiff")
        self.unique_act_products_locator = page.get_by_test_id("uniqueActiveProducts")
        self.active_companies_locator = page.get_by_test_id("activeCompanies")
        self.top_company_locator = page.get_by_test_id("topCompany")
        self.top_product_locator = page.get_by_test_id("topProduct")


        # Top 5 widget locators
        self.top_by_sales_widget_title_locator = page.get_by_text("Top 5 by Sales")
        self.top_by_sales_widget_subheader_locator = page.get_by_test_id("topSales").get_by_text("2028")
        self.top_by_sales_product_tab_locator = page.get_by_test_id("topSales").get_by_role("button", name="Product")
        self.top_by_sales_companies_tab_locator = page.get_by_role("button", name="Companies")
        self.top_by_sales_technology_tab_locator = page.get_by_role("button", name="Technology")
        self.top_by_sales_moa_tab_locator = page.get_by_role("button", name="MoA")
        #self.top_by_sales_expand_icon_locator = page.
        #self.top_by_sales_narrow_icon_locator = page.

        # Sales tab locators

        # Pipeline tab locators

        # Company tab locators

    def open_overview_tab(self):
        self.overview_tab_locator.click()

    def open_sales_tab(self):
        self.sales_tab_locator.click()

    def open_pipeline_tab(self):
        self.pipeline_tab_locator.click()

    def open_company_tab(self):
        self.company_tab_locator.click()

    def click_logout_button(self):
        self.logout_btn_locator.click()

    def expand_widget(self):
        self.top_by_sales_expand_icon_locator.click()

    def narrow_widget(self):
        self.top_by_sales_narrow_icon_locator.click()

    def select_companies_tab(self):
        self.top_by_sales_companies_tab_locator.click()

    def select_technology_tab(self):
        self.top_by_sales_technology_tab_locator.click()

    def select_moa_tab(self):
        self.top_by_sales_moa_tab_locator.click()

    def select_product_tab(self):
        self.top_by_sales_product_tab_locator.click()

