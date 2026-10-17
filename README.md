# PyTest Playwright Framework

A Python UI test automation project built with Pytest and Playwright. It uses the Page Object Model to keep page interactions separate from test cases, and loads the application URL and login test data from configuration files.

## Requirements

- Python 3.10 or newer
- Firefox
- The Python packages listed in `requirements.txt`
- The Pytest Playwright and HTML-report plugins (needed by the options in `pytest.ini`)

## Setup

From the project root, create and activate a virtual environment, then install the project and runner dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install pytest-playwright pytest-html
python -m playwright install firefox
```

If PowerShell blocks virtual-environment activation, run the commands using the Python executable directly from `.venv\Scripts\python.exe` instead.

## Configuration and test data

- Set `base_url` in `config/config.yaml` to the application under test. The `login_page` fixture reads this value before navigating to the site.
- `pages/login_page.py` reads the first row of `test_data/common_data.csv`. Keep the `email` and `password` column headers, and provide credentials for a dedicated test account.
- Do not store production credentials in the CSV or commit real credentials to source control. Use a local, ignored credentials file or another approved secret store for sensitive values.

## Running tests

Run the full suite:

```powershell
pytest
```

Run the dashboard login test only:

```powershell
pytest tests/UI_test/test_dashboard.py
```

Run tests carrying the authentication marker:

```powershell
pytest -m auth
```

Pytest settings in `pytest.ini` select Firefox, set a slow-motion delay, and enable tracing and video retention on failure plus screenshots on failure. The current test suite contains a login/dashboard UI test marked `auth`.

## Reports and logs

- HTML test report: `reports/report.html`
- Playwright run output, including retained failure artifacts: `test-results/`
- Pytest log: `logs/pytest_execution.log`
- Framework execution log: `logs/execution_<date>.log`

## Project layout

```text
.
├── config/
│   └── config.yaml             # Application base URL
├── pages/
│   ├── base_page.py            # Shared page operations
│   ├── dashboard_page.py       # Dashboard locators and checks
│   └── login_page.py           # Login locators and actions
├── test_data/
│   └── common_data.csv         # Login test data (keep credentials non-production)
├── tests/
│   └── UI_test/
│       └── test_dashboard.py   # Login and dashboard UI test
├── utils/
│   ├── config_reader.py        # YAML configuration loader
│   ├── file_utilities.py       # Test-data file helpers
│   └── logger.py               # Framework logging
├── conftest.py                 # Shared fixtures and browser logging
├── pytest.ini                  # Pytest and Playwright settings
└── requirements.txt            # Core Python dependencies
```
