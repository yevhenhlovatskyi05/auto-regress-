import os

import pytest

BASE_URL = os.environ.get("RC_BASE_URL", "https://shop-rc.artpix3d.com")


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    args = {**browser_context_args, "base_url": BASE_URL}

    user = os.environ.get("RC_BASIC_AUTH_USER")
    password = os.environ.get("RC_BASIC_AUTH_PASS")
    if user and password:
        args["http_credentials"] = {"username": user, "password": password}

    return args


@pytest.fixture
def ctx(context):
    return context


def dismiss_country_modal(page):
    dialog = page.get_by_role("dialog")
    if dialog.is_visible():
        dialog.get_by_role("button", name="save").click()
        dialog.wait_for(state="hidden")
