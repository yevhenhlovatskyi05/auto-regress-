import re

from playwright.sync_api import expect

from conftest import dismiss_country_modal

BASE_URL = "https://shop-rc.artpix3d.com"


def test_track_order_via_order_number_and_email(page):
    page.goto(f"{BASE_URL}/track-order/")
    dismiss_country_modal(page)

    page.get_by_role("button", name="Order Number").click()
    page.locator("#order_id").fill("7172447")
    page.locator('input#email[autocomplete="off"]').fill("yevhen.hlovatskyi@artpix3d.com")
    page.get_by_role("button", name="Track", exact=True).click()

    page.wait_for_url(re.compile(r"order_id=7172447"))
    assert "order_id=7172447" in page.url

    expect(page.get_by_role("heading", name="Order Tracking")).to_be_visible()
    expect(page.get_by_text("7172447").first).to_be_visible()
    expect(page.get_by_text("Shipment Information")).to_be_visible()
    expect(page.get_by_text("Shipping Address")).to_be_visible()
    expect(page.get_by_text("Processing", exact=True).first).to_be_visible()
    expect(page.get_by_text("Shipped", exact=True).first).to_be_visible()
    expect(page.get_by_text("Delivered", exact=True).first).to_be_visible()


def test_track_order_via_tracking_number(page):
    page.goto(f"{BASE_URL}/track-order/")
    dismiss_country_modal(page)

    page.get_by_role("button", name="Tracking Number").click()
    page.locator("#track_number").fill("397907444798")
    page.get_by_role("button", name="Track", exact=True).click()

    expect(page.get_by_role("heading", name="Order Tracking")).to_be_visible()
    expect(page.get_by_text("Processing", exact=True).first).to_be_visible()
    expect(page.get_by_text("Shipped", exact=True).first).to_be_visible()
    expect(page.get_by_text("Delivered", exact=True).first).to_be_visible()
