from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from utils.file_utilities import FileUtility
from utils.env_reader import get_env_variable
class LoginPage(BasePage):
    
    # email = FileUtility.read_csv_file("./test_data/common_data.csv", "email", 0)
    email = get_env_variable("email")
    # password = FileUtility.read_csv_file("./test_data/common_data.csv", "password", 0)
    password = get_env_variable("password")

    def __init__(self, page: Page):
        super().__init__(page)
        
        self.password_input = page.locator("//input[@name='password']")
        self.submit_btn = page.locator("//button[@type='submit']")
        self.forget_link = page.get_by_role("link", name="forget password?")
        self.email_input = page.locator("//input[@name='email']")
        self.signup_link = page.get_by_role("link", name="Create an account")
        
        
    def login(self, email: str = email, password: str = password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_btn.click()
        