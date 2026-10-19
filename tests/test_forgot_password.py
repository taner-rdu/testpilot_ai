from playwright.sync_api import Page, expect


def test_forgot_password_sends_reset_email(page: Page):
    page.goto("/forgot-password")

    page.locator("#emaail").fill("user@example.com")
    page.get_by_role("button", name="Retrieve password").click()

    expect(page.get_by_text("Password reset", exact=True)).to_be_visible()
    expect(page.get_by_text("An e-mail has been sent to you which explains how to reset your password.")).to_be_visible()
