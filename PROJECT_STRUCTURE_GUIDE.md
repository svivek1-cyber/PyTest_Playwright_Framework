# Pytest Framework Project Structure Guide

## Overview - Comparison with Maven

If you know Maven, think of this structure like this:

| Maven              | Pytest Project          | Purpose                               |
| ------------------ | ----------------------- | ------------------------------------- |
| `pom.xml`        | `requirements.txt`    | Dependency Management                 |
| `src/test/java`  | `tests/`              | Test Files                            |
| `src/main/java`  | `pages/` + `utils/` | Source Code (Page Objects, Utilities) |
| `target/`        | `reports/`            | Build Output (Test Reports)           |
| `pom.xml` config | `pytest.ini`          | Framework Configuration               |

---

## 📁 Project Root Files

### 1. **requirements.txt**

```
PURPOSE: Like Maven's pom.xml - lists all Python dependencies
STORES: Package names and versions needed to run the project
USES: 
  - pytest: Test framework (like JUnit & TestNG)
  - selenium: Browser automation library
  - pytest-html: Generate HTML test reports

HOW IT WORKS:
  - Run: pip install -r requirements.txt (installs all dependencies)
  - Similar to: mvn install (downloads dependencies)
```

### 2. **pytest.ini**

```
PURPOSE: Like pom.xml's <build> section - configures pytest behavior
STORES: Pytest settings and default configurations
USES:
  - testpaths = tests : Tells pytest to look for tests in 'tests' folder
  - Can also configure log levels, markers, plugins, etc.

EXAMPLE CONFIGS (like Maven plugins):
  - testpaths: Which directories contain tests
  - addopts: Default command-line options when running tests
  - markers: Custom test markers for categorization
```

### 3. **conftest.py**

```
PURPOSE: Like a test setup file - shared test fixtures and hooks
STORES: Pytest fixtures (reusable setup/teardown code)
USES:
  - Define fixtures used by ALL tests
  - Setup and teardown logic (like @Before/@After in JUnit)
  - Runs before tests execute

EXAMPLE:
  @pytest.fixture
  def setup():
      print('Setup browser')  # This runs before each test
      yield              # Test runs here
      print('Teardown')  # This runs after each test
```

### 4. **README.md**

```
PURPOSE: Documentation file
STORES: Project information, how to run tests, setup instructions
USES: Help developers understand and use the project
```

---

## 📁 Directory Structure & Purpose

```
pytest-framework/
│
├── 📄 pytest.ini              → Configuration file (like pom.xml settings)
├── 📄 conftest.py             → Global test fixtures and hooks
├── 📄 requirements.txt         → Python dependencies (like pom.xml)
├── 📄 README.md               → Project documentation
│
├── 📂 config/                 ⭐ Configuration & Environment Setup
│   ├── config.yaml            → Environment variables (base URL, timeout, etc.)
│   └── env.json               → Different env configs (dev, staging, prod)
│
├── 📂 pages/                  ⭐ Page Object Models (POM)
│   ├── login_page.py          → Login page elements & methods
│   └── cart_page.py           → Cart page elements & methods
│   
│   PURPOSE: Encapsulate UI elements and actions (like Java page classes)
│   STORES: Locators (XPath, CSS selectors), page methods
│   USES: Used by test files to interact with web pages
│
├── 📂 utils/                  ⭐ Utility/Helper Functions
│   ├── driver_factory.py      → Create WebDriver instances
│   ├── config_reader.py       → Read configuration files
│   └── logger.py              → Custom logging functionality
│   
│   PURPOSE: Reusable code (like utility classes in Java)
│   STORES: Helper functions and utilities
│   USES: Used by pages and tests for common operations
│
├── 📂 tests/                  ⭐ Test Files (Like src/test/java)
│   ├── test_login.py          → Login functionality tests
│   └── test_cart.py           → Cart functionality tests
│   
│   PURPOSE: Contains actual test cases
│   STORES: Test methods with @pytest.mark.* decorators
│   USES: Run with 'pytest' command to execute all tests
│
├── 📂 test_data/              ⭐ Test Input Data
│   └── users.json             → User credentials, test data
│   
│   PURPOSE: Store test data instead of hardcoding in tests
│   STORES: JSON/CSV files with test inputs
│   USES: Read by tests for parameterized testing
│
├── 📂 reports/                ⭐ Output - Test Reports
│   └── report.html            → Generated HTML test report
│   
│   PURPOSE: Stores test results and reports (like Maven target/)
│   STORES: HTML reports, XML reports
│   USES: View test results in browser (pytest-html plugin creates this)
│   AUTO-GENERATED: Yes, recreated after each test run
│
├── 📂 logs/                   ⭐ Output - Log Files
│   └── (test logs go here)    → Application and test logs
│   
│   PURPOSE: Stores execution logs
│   STORES: Log files with timestamps
│   USES: Debug test failures by reviewing logs
│   AUTO-GENERATED: Yes, created during test execution
│
└── 📂 screenshots/            ⭐ Output - Evidence
    └── (failure screenshots)  → Screenshots on test failure
  
    PURPOSE: Visual evidence of test failures
    STORES: PNG/JPG screenshots
    USES: Understand what went wrong visually
    AUTO-GENERATED: Yes, when test fails
```

---

## 🔄 How it All Works Together

### Execution Flow (Like Maven Test Execution)

```
1. pytest command triggered
   ↓
2. pytest.ini loaded (configuration)
   ↓
3. conftest.py executed (global fixtures)
   ↓
4. tests/ folder scanned for test files
   ↓
5. Each test_*.py file executed
   ↓
6. For each test:
   - conftest.py fixture (setup) executes
   - pages/ methods use utils/ helpers
   - test_data/ loaded as needed
   - Test executes
   - conftest.py fixture (teardown) executes
   - Screenshots/Logs saved on failure
   ↓
7. reports/ folder gets new HTML report
   ↓
8. Test run complete
```

---

## 📊 Input vs Output Folders

### INPUT FOLDERS (What you create/maintain):

- **config/** - Environment & settings (YOU maintain)
- **pages/** - Page objects (YOU write)
- **tests/** - Test cases (YOU write)
- **test_data/** - Test data files (YOU create)
- **utils/** - Helper functions (YOU create)

### OUTPUT FOLDERS (Auto-generated by tests):

- **reports/** - HTML/XML reports (PYTEST creates)
- **logs/** - Execution logs (TESTS create)
- **screenshots/** - Failure evidence (TESTS create)

---

## 🚀 Common Commands

```bash
# Install dependencies (like mvn install)
pip install -r requirements.txt

# Run all tests (like mvn test)
pytest

# Run specific test file (like mvn test -Dtest=LoginTest)
pytest tests/test_login.py

# Run with HTML report (like Maven Surefire)
pytest --html=reports/report.html

# Run with verbose output (like mvn -X)
pytest -v

# Run with logging (like debug mode)
pytest --log-cli-level=INFO

# Stop on first failure (like failfast)
pytest -x

# Show print statements (like System.out)
pytest -s
```

---

## 💡 Key Concepts

### 1. **Page Object Model (POM)** - pages/

- Separates test logic from page elements
- Like having separate Java classes for each web page
- Makes tests more maintainable

### 2. **Fixtures** - conftest.py

- Setup/teardown code reused across tests
- Like @Before/@After annotations in JUnit
- Centralized in conftest.py

### 3. **Test Data** - test_data/

- Separates data from test logic
- Makes tests reusable with different data
- Like parameterized tests in JUnit

### 4. **Utilities** - utils/

- Common functions used across project
- driver_factory: Creates browser instances
- config_reader: Reads settings
- logger: Logging functionality

---

## 🎯 Best Practices

```
✅ DO:
- Keep test logic in tests/
- Keep page elements in pages/
- Keep helpers in utils/
- Keep test data in test_data/
- Use fixtures for setup/teardown
- Use page objects to interact with UI

❌ DON'T:
- Hardcode URLs/data in tests
- Mix page logic with test logic
- Duplicate code - use utils instead
- Ignore logs and screenshots on failure
```

---

## 📝 Typical Test File Example

```python
# tests/test_login.py

import pytest
from pages.login_page import LoginPage  # Import page object
from utils.driver_factory import DriverFactory  # Import utility
from utils.config_reader import ConfigReader  # Import config

class TestLogin:
  
    @pytest.fixture(autouse=True)  # Runs before each test in this class
    def setup(self):
        self.driver = DriverFactory.get_driver()
        self.config = ConfigReader.get_config()
        yield
        self.driver.quit()  # Cleanup after test
  
    def test_valid_login(self):
        """Test login with valid credentials"""
        # Arrange: Setup test data
        login_page = LoginPage(self.driver)
  
        # Act: Perform actions
        login_page.login("user@example.com", "password123")
  
        # Assert: Verify results
        assert login_page.is_dashboard_displayed()
```

---

## 🔗 Comparison Matrix

| Feature           | Maven (Java)            | Pytest (Python)      |
| ----------------- | ----------------------- | -------------------- |
| Dependency File   | pom.xml                 | requirements.txt     |
| Config File       | pom.xml (build section) | pytest.ini           |
| Fixtures/Setup    | JUnit @Before/@After    | conftest.py fixtures |
| Test Folder       | src/test/java           | tests/               |
| Source Code       | src/main/java           | pages/ + utils/      |
| Reports           | target/                 | reports/             |
| Build Command     | mvn clean test          | pytest               |
| Package Structure | com.company.package     | python package names |
