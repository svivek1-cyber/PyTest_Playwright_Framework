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
    # login_page.page.wait_for_timeout(2000)  # Wait for 2 seconds to observe the dashboard

@pytest.mark.auth
def test_login_with_invalid_credentials(login_page: LoginPage):
    file_utility = FileUtility()
    invalid_email = file_utility.read_excel_file("D:\\Desktop\\PlayWright\\PyTest_Playwright_Framework\\test_data\\testdata.xlsx", "LoginPageData", 0, 0)
    invalid_password = file_utility.read_excel_file("D:\\Desktop\\PlayWright\\PyTest_Playwright_Framework\\test_data\\testdata.xlsx", "LoginPageData", 1, 0)
    login_page.login(invalid_email, invalid_password)
    expect(login_page.invalid_credentials_error).to_be_visible()
    # login_page.page.wait_for_timeout(2000)  # Wait for 2 seconds to observe the error message