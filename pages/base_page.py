from playwright.sync_api import Page, Locator

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, path: str = ""):
        self.page.goto(path)

    def wait_for_url(self, url: str):
        self.page.wait_for_url(url)