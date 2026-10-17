import pytest
from playwright.sync_api import Page, expect
from pages.dashboard_page import DashboardPage
from utils.file_utilities import FileUtility
from pages.login_page import LoginPage

@pytest.mark.auth
def test_login(login_page: LoginPage):
    login_page.login()
    dashboard_page = DashboardPage(login_page.page)
    dashboard_page.verify_dashboard()
    login_page.page.wait_for_timeout(2000)  # Wait for 2 seconds to observe the dashboard
    