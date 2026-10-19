from playwright.sync_api import Page, expect


def test_locators_page_elements(page: Page):
    page.goto("/locators")

    expect(page.get_by_role("heading", level=1)).to_contain_text("Locators Test page")
    expect(page.get_by_role("button", name="Add Item")).to_be_visible()
    expect(page.get_by_role("link", name="Contact")).to_have_attribute("href", "/contact")
    expect(page.get_by_text("Hot Deal: Buy 1 Get 1 Free")).to_be_visible()

    page.locator("#countrySelect").select_option(label="Japan")
    expect(page.locator("#countrySelect")).to_have_value("Japon")

    expect(page.get_by_test_id("status-message")).to_contain_text("All systems operational")
    expect(page.get_by_test_id("user-name")).to_contain_text("Username: Alice")
