import os
import pytest
from playwright.sync_api import expect


@pytest.mark.usefixtures("setup")
class TestShareFunc:

    def test_cancel_sharing(self, login_to_app, markets_page):
        page = markets_page.page

        markets_page.select_companies_tab()
        markets_page.share_btn_locator.click()
        markets_page.share_modal_x_icon_locator.click()
        expect(markets_page.share_modal_cancel_btn_locator).not_to_be_visible()

        markets_page.share_btn_locator.click()
        markets_page.share_modal_cancel_btn_locator.click()
        expect(markets_page.share_modal_cancel_btn_locator).not_to_be_visible()
        clipboard_text = page.evaluate('() => navigator.clipboard.readText()')
        assert os.environ["URL"] + "/dashboard/market-sizing/overview" not in clipboard_text

    def test_share_functionality(self, markets_page):
        page = markets_page.page

        markets_page.click_here_to_nav_to_dashboard()

        expect(markets_page.share_btn_locator).to_be_visible()

        markets_page.share_btn_locator.click()
        expect(markets_page.share_modal_title_locator).to_have_text("Share Dashboard")
        expect(markets_page.share_modal_x_icon_locator).to_be_visible()
        expect(markets_page.share_modal_text_locator).to_have_text("Click Copy Link to share this dashboard.")
        expect(markets_page.share_modal_copy_btn_locator).to_be_visible()
        expect(markets_page.share_modal_cancel_btn_locator).to_be_visible()

        markets_page.share_modal_copy_btn_locator.click()
        expect(markets_page.share_toast_msg_locator).to_be_visible()
        expect(markets_page.share_modal_cancel_btn_locator).not_to_be_visible()

        clipboard_text = page.evaluate('() => navigator.clipboard.readText()')
        assert os.environ["URL"] + "/dashboard/market-sizing/overview" in clipboard_text

    def test_share_with_not_authorized_user(self, markets_page):
        page = markets_page.page

        markets_page.click_here_to_nav_to_dashboard()
        markets_page.share_btn_locator.click()
        markets_page.share_modal_copy_btn_locator.click()

        clipboard_text = page.evaluate('() => navigator.clipboard.readText()')

        markets_page.click_logout_button()

        page.goto(clipboard_text)

        expect(markets_page.logout_btn_locator).not_to_be_visible()
