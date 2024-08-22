# wap-test-python

This project is designed to automate interactions with the Twitch website using Selenium and Python. The project is structured to follow best practices, including the use of the Page Object Model (POM) and a modular approach for maintainability and scalability.

## Demo

![Tests Running](./assets/wap_test_2024-08-21at18.gif)

## Folder Structure

The project is organized as follows:

```plaintext
├── config/
│ ├── config.py # Configuration settings such as URLs, constants, etc.
│ └── pytest.ini # Pytest configuration file
├── pages/
│ ├── base_page.py # BasePage class containing common methods for all page objects
│ └── twitch_page.py # TwitchPage class representing the Twitch page and its actions
├── tests/
│ ├── base_test.py # BaseTest class containing common setup and teardown for tests
│ └── test_twitch.py # Test cases for Twitch page functionalities
├── .gitignore # Git ignore file to exclude unnecessary files from version control
├── Pipfile # Pipenv file specifying project dependencies
├── Pipfile.lock # Pipenv lock file to ensure deterministic builds
└── README.md # Project documentation (this file)
```

## Setup

### Prerequisites

- Python 3.11.x
- Pipenv (for managing virtual environments and dependencies)
- Google Chrome and ChromeDriver

### Installing Dependencies

First, ensure that you have `pipenv` installed:

```bash
pip install pipenv
```

Next, install the project dependencies using `pipenv`:

```bash
pipenv install
```

## Running Tests

To run the test cases, execute the following command:

```bash
pipenv run pytest
```
