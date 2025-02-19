from playwright.sync_api import Page

class BasePage:

    PAGE_URL = "https://autofaq.ai/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.PAGE_URL)

    def find(self, locator):
        return self.page.locator(locator)