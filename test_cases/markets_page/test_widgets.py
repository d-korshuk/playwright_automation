import pytest
from playwright.sync_api import expect


@pytest.mark.usefixtures("setup")
class TestWidgets:

    def test_expand_narrow_widget(self, login_to_app, markets_page):
        expect(markets_page.develop_status_expand_icon_locator).to_be_visible()

        markets_page.develop_status_expand_icon_locator.click()
        expect(markets_page.develop_status_collapse_icon_locator).to_be_visible()
        expect(markets_page.develop_status_expand_icon_locator).not_to_be_visible()

        markets_page.develop_status_collapse_icon_locator.click()
        expect(markets_page.develop_status_expand_icon_locator).to_be_visible()

    def test_switch_widget_tabs(self, login_to_app, markets_page):
        expect(markets_page.develop_status_prod_count_tab_locator).to_have_attribute("aria-pressed", "true")
        expect(markets_page.develop_status_prod_w_sales_locator).to_have_attribute("aria-pressed", "false")

        markets_page.develop_status_prod_w_sales_locator.click()
        expect(markets_page.develop_status_prod_count_tab_locator).to_have_attribute("aria-pressed", "false")
        expect(markets_page.develop_status_prod_w_sales_locator).to_have_attribute("aria-pressed", "true")
