from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class DashboardPage(BasePage):
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.z_symbol = page.locator("//div[text()='Z']")
        
    def verify_dashboard(self: None):
        expect(self.z_symbol).to_be_visible()
        