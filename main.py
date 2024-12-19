from playwright.sync_api import Page, expect


def test_example(page: Page):
    page.goto('')
    page.locator('')
    expect(page.locator('')).to_have_text()
