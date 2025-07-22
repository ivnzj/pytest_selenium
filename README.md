# Pytest selenium / api playground

This repository is a playground for experimenting with UI (Selenium) and API (requests-based) tests using the pytest framework. It demonstrates practical automation techniques including cookie handling, CAPTCHA workarounds and POM.

## Prerequisites

This project is developed and tested on the following stack:

- OS: **Ubuntu 22.04**
- Python: **3.10.12**
- Google Chrome: **Latest stable version**
- Display resolution: **1920 x 1080** (required for consistent Selenium test execution)

## Installation

To set up the test environment:

```bash
./setup.sh
```

This script will:

- Create a Python virtual environment.
- Install all dependencies listed in `requirements.txt`.

## Test Execution

To execute all tests and generate an HTML report:

```bash
./run.sh
```

### Notes

- **Some API tests are expected to fail**, as the endpoints behave differently than expected.  
- **CAPTCHA Handling:** UI tests occasionally (and often) encounter CAPTCHA screens. Several workarounds have been attempted based on common online: slowing down interactions (e.g., typing or clicking), using fake user agents, running in headless mode or adjusting wait times—but these have had limited success. If a CAPTCHA does appear, the test will pause and allow the user up to 120 seconds to manually solve it. Once resolved, the test execution will resume automatically.

Expected final result is 9 passed and 5 failed tests.

## TODO

Planned improvements and tasks:

- [ ] Implement test logger
- [ ] Capture screenshots on test failure
- [ ] Add an API client wrapper
- [ ] Fully automate environment setup:
  - [ ] Enable WSL
  - [ ] Install Ubuntu 22.04
  - [ ] Install Python 3.x
  - [ ] Install Chrome
- [ ] Enable parallel execution of UI and API tests
- [ ] Add test tagging with `pytest.mark` for easier filtering and execution
- [ ] Implement CAPTCHA bypass/workaround

## Project Structure

```text
.
├── setup.sh                # Environment setup script
├── requirements.txt        # Dependencies for pytest
├── tests/                  # Test cases
│   ├── api/                # API test cases and helper utilities
│   └── ui/                 # UI test cases and helper utilities
├── reports/                # HTML test reports
├── pages/                  # Page Object Models for Selenium
└── README.md               # Project documentation

```
