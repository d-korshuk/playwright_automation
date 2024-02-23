import random
import pytest
from playwright.sync_api import expect


@pytest.mark.usefixtures("setup")
class TestSalesDateRange:

    def test_sales_date_range_selection(self, login_to_app, markets_page):
        expect(markets_page.from_dropdown_locator).to_be_visible()
        expect(markets_page.from_dropdown_locator).to_have_text("2022")

        markets_page.open_from_dropdown()

        expect(markets_page.get_from_dropdown_year_locator("1984")).to_be_visible()
        expect(markets_page.get_from_dropdown_year_locator("2028")).to_be_visible()

        selected_from_year = str(random.randint(1984, 2028))
        markets_page.select_from_year_item(selected_from_year)

        markets_page.from_dropdown_locator = markets_page.page.get_by_test_id("boxRangeSelector").locator("div").filter(
            has_text=selected_from_year).nth(3)
        expect(markets_page.from_dropdown_locator).to_be_visible()

        markets_page.open_to_dropdown()

        expect(markets_page.get_to_dropdown_year_locator("1984")).to_be_visible()
        expect(markets_page.get_to_dropdown_year_locator("2028")).to_be_visible()

        selected_to_year = str(random.randint(1984, 2028))
        markets_page.select_to_year_item(selected_to_year)
        markets_page.to_dropdown_locator = markets_page.page.get_by_test_id("boxRangeSelector").locator("div").filter(
            has_text=selected_from_year).nth(3)

        expect(markets_page.to_dropdown_locator).to_be_visible()

    def test_select_equal_years(self, login_to_app, markets_page):
        markets_page.open_from_dropdown()
        selected_from_year = "2015"
        markets_page.select_from_year_item(selected_from_year)
        markets_page.from_dropdown_locator = markets_page.page.get_by_test_id("boxRangeSelector").locator("div").filter(
            has_text=selected_from_year).nth(3)

        markets_page.open_to_dropdown()
        selected_to_year = "2015"
        markets_page.select_to_year_item(selected_to_year)
        markets_page.to_dropdown_locator = markets_page.page.get_by_test_id("boxRangeSelector").locator("div").filter(
            has_text=selected_to_year).nth(3)

        expect(markets_page.from_dropdown_locator).to_have_text(selected_from_year)
        expect(markets_page.to_dropdown_locator).to_have_text(selected_to_year)

    @pytest.mark.sales
    def test_from_cant_be_greater_than_to(self, login_to_app, markets_page):

        markets_page.open_to_dropdown()
        selected_to_year = str(random.randint(1984, 2021))
        markets_page.select_to_year_item(selected_to_year)
        markets_page.to_dropdown_locator = markets_page.page.get_by_test_id("boxRangeSelector").locator("div").filter(
            has_text=selected_to_year).nth(3)

        expect(markets_page.to_dropdown_locator).not_to_be_visible()
