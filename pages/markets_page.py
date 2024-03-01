from playwright.sync_api import Page


class MarketsPage:
    def __init__(self, page=Page):
        self.page = page

        #General locators
        self.page_logo = page.get_by_test_id("AutoGraphIcon")
        self.page_title = page.get_by_text("Markets")
        self.overview_tab_locator = page.get_by_role("tab", name="overview")
        self.sales_tab_locator = page.get_by_role("tab", name="sales")
        self.pipeline_tab_locator = page.get_by_role("tab", name="pipeline")
        self.company_tab_locator = page.get_by_role("tab", name="company")
        self.logout_btn_locator = page.get_by_role("button", name="Logout")
        self.click_to_nav_to_dashboard = page.get_by_role("link", name="here")

        # Overview tab locators
        self.overview_wwsales_2022_locator = page.get_by_test_id("worldwideSalesStart")
        self.overview_wwsales_2028_locator = page.get_by_test_id("worldwideSalesEnd")
        self.overview_wwsales_2028_diff_locator = page.get_by_test_id("worldwideSalesDiff")
        self.overview_unique_act_products_locator = page.get_by_test_id("uniqueActiveProducts")
        self.overview_active_companies_locator = page.get_by_test_id("activeCompanies")
        self.overview_top_company_locator = page.get_by_test_id("topCompany")
        self.overview_top_product_locator = page.get_by_test_id("topProduct")

        # Top 5 widget locators
        self.top_by_sales_widget_title_locator = page.get_by_text("Top 5 by Sales")
        self.top_by_sales_widget_subheader_locator = page.get_by_test_id("topSales").get_by_text("2029")
        self.top_by_sales_product_tab_locator = page.get_by_test_id("topSales").get_by_role("button", name="Product")
        self.top_by_sales_companies_tab_locator = page.get_by_role("button", name="Companies")
        self.top_by_sales_technology_tab_locator = page.get_by_role("button", name="Technology")
        self.top_by_sales_moa_tab_locator = page.get_by_role("button", name="MoA")
        # self.top_by_sales_expand_icon_locator = page.
        # self.top_by_sales_narrow_icon_locator = page.

        # Sales tab locators
        self.sales_wwsales_2023_locator = page.get_by_test_id("worldwideSalesStart")
        self.sales_wwsales_2029_locator = page.get_by_test_id("worldwideSalesEnd")
        self.sales_cagr_locator = page.get_by_test_id("cagr")
        self.sales_wwsales_2029_diff_locator = page.get_by_test_id("worldwideSalesDiff")

        # Pipeline tab locators
        self.pipeline_products_locator = page.get_by_test_id("products")
        self.pipeline_products_by_indication_locator = page.get_by_test_id("productsIndication")
        self.pipeline_companies_locator = page.get_by_test_id("companies")
        self.pipeline_indications_locator = page.get_by_test_id("indications")

        # Company tab locators
        self.company_active_companies_locator = page.get_by_test_id("activeCompanies")
        self.company_wwsales_2023_locator = page.get_by_test_id("worldwideSalesStart")
        self.company_wwsales_2029_locator = page.get_by_test_id("worldwideSalesEnd")
        self.company_wwsales_2029_diff_locator = page.get_by_test_id("worldwideSalesDiff")
        self.company_cagr_locator = page.get_by_test_id("cagr")
        self.company_listed_locator = page.get_by_test_id("listedCompanies")
        self.company_private_locattor = page.get_by_test_id("privateCompanies")
        self.company_pjv_locator = page.get_by_test_id("privateJVCompanies")

        # Global Filters locators
        self.global_filters_collapse_icon_locator = page.get_by_test_id("drawer-btn")
        self.global_filters_clear_all_btn_locator = page.get_by_role("button", name="Clear all")

        # Sales Date Range locators
        self.from_dropdown_locator = page.get_by_test_id("boxRangeSelector").locator("div").filter(has_text="2023").nth(
            3)
        self.to_dropdown_locator = page.get_by_test_id("boxRangeSelector").locator("div").filter(has_text="2029").nth(3)



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

    # def expand_widget(self):
    #    self.top_by_sales_expand_icon_locator.click()

    # def narrow_widget(self):
    #    self.top_by_sales_narrow_icon_locator.click()

    def select_companies_tab(self):
        self.top_by_sales_companies_tab_locator.click()

    def select_technology_tab(self):
        self.top_by_sales_technology_tab_locator.click()

    def select_moa_tab(self):
        self.top_by_sales_moa_tab_locator.click()

    def select_product_tab(self):
        self.top_by_sales_product_tab_locator.click()

    def open_from_dropdown(self):
        self.from_dropdown_locator.click()

    def open_to_dropdown(self):
        self.to_dropdown_locator.click()

    def get_from_dropdown_year_locator(self, year):
        return self.page.get_by_role("option", name=str(year))

    def get_to_dropdown_year_locator(self, year):
        return self.page.get_by_role("option", name=str(year))

    def select_from_year_item(self, year):
        year_locator = self.get_from_dropdown_year_locator(year)
        year_locator.click()

    def select_to_year_item(self, year):
        year_locator = self.get_to_dropdown_year_locator(year)
        year_locator.click()

    def click_here_to_nav_to_dashboard(self):
        self.click_to_nav_to_dashboard.click()
