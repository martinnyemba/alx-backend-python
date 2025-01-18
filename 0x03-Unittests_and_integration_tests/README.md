# ALX Backend Python - Unittests and Integration Tests

## Project Overview
This project focuses on implementing unit tests and integration tests in Python, specifically covering the testing of nested map access, HTTP calls, and Github organization client functionality.

## Requirements
- Ubuntu 18.04 LTS
- Python 3.7
- pycodestyle (version 2.5)
- unittest
- unittest.mock
- parameterized
- requests library

## Project Structure
```
0x03-Unittests_and_integration_tests/
│
├── test_utils.py           # Tests for utils functions
├── test_client.py         # Tests for Github client
├── utils.py               # Utility functions
├── client.py             # Github organization client
├── fixtures.py           # Test fixtures
└── README.md
```

## Key Features
1. Unit Tests:
   - Parameterized testing of nested map access
   - Exception testing
   - Mocking HTTP calls
   - Testing memoization

2. Integration Tests:
   - Github organization client testing
   - Fixtures implementation
   - Request mocking
   - License checking

## Test Cases

### Utils Tests (`test_utils.py`)
- `TestAccessNestedMap`: Tests nested map access functionality
- `TestGetJson`: Tests JSON retrieval from HTTP calls
- `TestMemoize`: Tests memoization decorator

### Client Tests (`test_client.py`)
- `TestGithubOrgClient`: Tests Github organization client
- `TestIntegrationGithubOrgClient`: Integration tests with fixtures

## Running Tests
```bash
# Run all tests
python -m unittest discover

# Run specific test file
python -m unittest test_utils.py
python -m unittest test_client.py
```

## Key Concepts Covered
- Unit testing vs Integration testing
- Test parameterization
- Mocking external calls
- Test fixtures
- Property mocking
- HTTP call mocking
- Exception testing
- Memoization testing

## Available Functions

### Utils Module
- `access_nested_map(nested_map, path)`
- `get_json(url)`
- `memoize(fn)`

### Client Module
- `GithubOrgClient` class methods:
  - `org()`
  - `_public_repos_url()`
  - `public_repos()`
  - `has_license(repo, license_key)`

## Development Guidelines
1. All files should start with shebang `#!/usr/bin/env python3`
2. Code should follow pycodestyle style (version 2.5)
3. All modules, classes, and functions must have documentation
4. All functions must include type annotations
5. Tests should mock external calls where appropriate

## Author
Nyemba Martin

## License
Copyright © 2025 ALX, All rights reserved.
