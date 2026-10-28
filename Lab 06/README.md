# Lab 6 – Code and Branch Coverage Analysis

**Student Name:** Renetta Isabel Nathan  
**SRN:** PES1UG24AM221

## Objective

To understand and measure code coverage and branch coverage using Python's `coverage` tool and `pytest`, and to develop test cases that achieve at least 90% coverage.

## Application

The application is `password_policy.py`. It checks password length, common passwords, uppercase and lowercase characters, digits, and special characters. It also evaluates password strength and suggests fixes for detected issues.

## Tools Used

- Python
- pytest
- coverage.py
- Google Colab

## Test Files

- `CodeCoverageTest_PES1UG24AM221_application.py`
- `BranchCoverageTest_PES1UG24AM221_application.py`

## Running Code Coverage

```bash
coverage erase
coverage run --include="*/password_policy.py" -m pytest -v CodeCoverageTest_PES1UG24AM221_application.py
coverage report -m
```

## Running Branch Coverage

```bash
coverage erase
coverage run --branch --include="*/password_policy.py" -m pytest -v BranchCoverageTest_PES1UG24AM221_application.py
coverage report -m
```

## Results

- Code coverage: 100% achieved.
- Branch coverage: Record the percentage shown in the final branch coverage report.
- Screenshots of both successful coverage reports are included in this folder.

## Conclusion

Test cases were created to exercise the password validation, password strength evaluation, and password fix suggestion functions. Code coverage was verified using `coverage.py`, and branch coverage was evaluated separately to check the execution of conditional outcomes.
