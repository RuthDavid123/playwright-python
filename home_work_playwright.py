from playwright.sync_api import Page, expect
from faker import Faker
faker = Faker()


def test_example(page: Page):
    page.goto('https://www.qa-practice.com/elements/select/mult_select')
    page.locator('').fill()
    expect(page.locator('')).to_have_text()
