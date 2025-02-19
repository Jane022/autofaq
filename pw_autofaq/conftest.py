
from faker import Faker
import pytest
import allure
import os

from playwright.sync_api import Page, sync_playwright

fake = Faker("ru_RU")

@pytest.fixture
def name():
    return fake.first_name()

@pytest.fixture
def email():
    return fake.email()

@pytest.fixture(scope="function")
def page() -> Page:
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

def save_screenshot(page, test_name):
    screenshot_path = f"screenshots/{test_name}.png"
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    page.screenshot(path=screenshot_path)
    allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)

def attach_video(page, test_name):
    video_path = f"videos/{test_name}.webm"
    if os.path.exists(video_path):
        allure.attach.file(video_path, name="Video", attachment_type=allure.attachment_type.WEBM)

@pytest.hookimpl
def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        page = item.funcargs.get('page')
        if page:
            save_screenshot(page, item.name)
            attach_video(page, item.name)