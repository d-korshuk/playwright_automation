from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.login_btn_header_locator = page.get_by_role("button", name="Log in")
        self.email_locator = "input[name='username']"
        self.next_btn_locator = "text=Next"
        self.password_locator = "input[id='password']"
        self.submit_btn_locator = page.locator('button:has-text("Log in")')
        self.error_message_locator = page.locator('[data-error-code="wrong-email-credentials"]')

    def click_header_login_btn(self):
        self.login_btn_header_locator.click()

    def enter_email(self, email: str):
        self.page.wait_for_selector(self.email_locator).fill(email)

    def click_next_btn(self):
        self.page.wait_for_selector(self.next_btn_locator).click()

    def enter_password(self, password: str):
        password_input = self.page.wait_for_selector(self.password_locator)
        password_input.click()
        password_input.fill(password)

    def click_submit_button(self):
        self.submit_btn_locator.click()
