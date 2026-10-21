# fixtures are there
# import os
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from utils.env_reader import get_env_variable
from utils.logger import get_logger
from utils.config_reader import load_config

log = get_logger("Conftest")

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Sets a global default viewport and base URL."""
    return {
        **browser_context_args,
        "viewport": {"width": 1500, "height": 820},
        "ignore_https_errors": True,
    }

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    # base_url = os.getenv("BASE_URL")
    # if base_url is None:
    #     base_url = get_env_variable("BASE_URL")
        
    base_url = load_config()["base_url"]  # Load base_url from config.yaml

    page.goto(base_url)
    return LoginPage(page)


# log setup for each test
@pytest.fixture(autouse=True)
def setup_test_logging(page, request):
    test_name = request.node.name
    log.info(f"========== STARTING TEST: {test_name} ==========")

    # Intercept browser console logs (e.g. console.log, console.error)
    page.on("console", lambda msg: log.debug(f"[Browser Console {msg.type.upper()}] {msg.text}"))

    # Intercept unhandled JS exceptions on the web page
    page.on("pageerror", lambda exc: log.error(f"[Browser Exception] {exc}"))

    yield

    log.info(f"========== FINISHED TEST: {test_name} ==========\n")