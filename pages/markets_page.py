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
        self.diff_arrow_down_locator = page.get_by_test_id("ArrowDownwardIcon")
        self.diff_arrow_up_locator = page.get_by_test_id("ArrowUpwardIcon")

        # Share button locators
        self.share_btn_locator = page.get_by_role("button", name="Share")
        self.share_modal_title_locator = page.get_by_role("heading")
        self.share_modal_x_icon_locator = page.get_by_label("close")
        self.share_modal_text_locator = page.get_by_text("Click Copy Link to share this")
        self.share_modal_cancel_btn_locator = page.get_by_role("button", name="Cancel")
        self.share_modal_copy_btn_locator = page.get_by_role("button", name="Copy Link")
        self.share_toast_msg_locator = page.get_by_role("alert")

        # Overview tab locators
        self.overview_wwsales_2023_locator = page.get_by_test_id("worldwideSalesStart")
        self.overview_wwsales_2029_locator = page.get_by_test_id("noMetricsData")
        self.overview_wwsales_2029_diff_locator = page.get_by_test_id("worldwideSalesDiff")
        self.overview_unique_act_products_locator = page.get_by_test_id("uniqueActiveProducts")
        self.overview_active_companies_locator = page.get_by_test_id("activeCompanies")
        self.overview_top_company_locator = page.get_by_test_id("topCompany")
        self.overview_top_product_locator = page.get_by_test_id("topProduct")

        # Sales tab locators
        self.sales_wwsales_2023_locator = page.get_by_test_id("worldwideSalesStart")
        self.sales_wwsales_2029_locator = page.get_by_test_id("noMetricsData").first
        self.sales_wwsales_2029_diff_locator = page.get_by_test_id("worldwideSalesDiff")
        self.sales_cagr_locator = page.get_by_test_id("noMetricsData").nth(1)

        # Pipeline tab locators
        self.pipeline_products_locator = page.get_by_test_id("products")
        self.pipeline_products_by_indication_locator = page.get_by_test_id("productsIndication")
        self.pipeline_companies_locator = page.get_by_test_id("companies")
        self.pipeline_indications_locator = page.get_by_test_id("indications")

        # Company tab locators
        self.company_active_companies_locator = page.get_by_test_id("activeCompanies")
        self.company_wwsales_2023_locator = page.get_by_test_id("worldwideSalesStart")
        self.company_wwsales_2029_locator = page.get_by_test_id("noMetricsData").first
        self.company_wwsales_2029_diff_locator = page.get_by_test_id("worldwideSalesDiff")
        self.company_cagr_locator = page.get_by_test_id("noMetricsData").nth(1)
        self.company_listed_locator = page.get_by_test_id("listedCompanies")
        self.company_private_locator = page.get_by_test_id("privateCompanies")
        self.company_pjv_locator = page.get_by_test_id("privateJVCompanies")

        # Top 5 widget locators
        self.top_by_sales_widget_title_locator = page.get_by_text("Top 5 by Sales")
        self.top_by_sales_widget_subheader_locator = page.get_by_test_id("topSales").get_by_text("2029")
        self.top_by_sales_product_tab_locator = page.get_by_test_id("topSales").get_by_role("button", name="Product")
        self.top_by_sales_companies_tab_locator = page.get_by_role("button", name="Companies")
        self.top_by_sales_technology_tab_locator = page.get_by_role("button", name="Technology")
        self.top_by_sales_moa_tab_locator = page.get_by_role("button", name="MoA")

        # Development Status Summary widget locators
        self.develop_status_title_locator = page.get_by_text("Development Status Summary")
        self.develop_status_year_locator = page.get_by_test_id("developmentStatus").get_by_text("2029")
        self.develop_status_prod_count_tab_locator = page.get_by_role("button", name="Product Count")
        self.develop_status_prod_w_sales_locator = page.get_by_role("button", name="Products with Sales")
        self.develop_status_expand_icon_locator = page.get_by_test_id("developmentStatus").get_by_role("button").nth(2)
        self.develop_status_collapse_icon_locator = page.get_by_role("button").nth(2)
        self.develop_status_marketed_locator = page.get_by_text("Marketed")
        self.develop_status_approved_locator = page.get_by_text("Approved")
        self.develop_status_filed_locator = page.get_by_text("Filed")
        self.develop_status_phase3_locator = page.get_by_text("Phase III")
        self.develop_status_phase2_locator = page.get_by_text("Phase II", exact=True)
        self.develop_status_phase1_locator = page.get_by_text("Phase I", exact=True)
        self.develop_status_preclinical_locator = page.get_by_text("Pre-Clinical")
        self.develop_status_research_project_locator = page.get_by_text("Research Project")

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

    def paste_from_clipboard(self):
        self.page.keyboard.press("Control+V")
