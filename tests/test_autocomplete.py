from playwright.sync_api import Page, expect


def test_autocomplete_country_selection(page: Page):
    page.goto("/autocomplete")

    page.locator("#city").fill("Uni")
    suggestions = page.locator("#countryautocomplete-list div")
    expect(suggestions).to_have_count(3)

    suggestions.filter(has_text="United Kingdom").click()
    page.get_by_role("button", name="Submit").click()

    expect(page.locator("#result")).to_have_text("You selected: United Kingdom")
