# Lab 7 – Fuzz Testing for Input Validation Bugs

## Password Policy Checker

### Overview

This lab focused on applying **Fuzz Testing using the Hypothesis library** to identify and fix input validation bugs in a Python-based Password Policy Checker application.

The application contains three functions responsible for classifying password characters, splitting username-password credentials, and calculating the digit ratio of a password. Hypothesis was used to automatically generate different inputs, including empty strings and invalid values, to identify unexpected behaviour and application crashes.

The identified bugs were fixed using defensive programming techniques, and the corrected application was tested again using Pytest.

---

## Objectives

- Understand the purpose and methodology of fuzz testing.
- Apply property-based testing using the Hypothesis library.
- Automatically generate unexpected and malformed inputs.
- Identify edge-case bugs and unexpected exceptions.
- Improve application robustness through input validation and defensive programming.

---

## Technologies Used

- **Python 3** – Application development and testing.
- **Google Colab** – Execution environment.
- **Hypothesis** – Property-based fuzz testing.
- **Pytest** – Automated test execution.

---

## Project Structure

```text
lab7/
│
├── README.md
├── password_policy.py
└── test_password_policy.py
```

| File | Description |
|---|---|
| `password_policy.py` | Contains the Password Policy Checker functions and the main application. |
| `test_password_policy.py` | Contains Hypothesis-based fuzz tests for all three functions. |
| `README.md` | Documentation of the lab, testing methodology, and results. |

---

## Functions Tested

The application contains three main functions:

### 1. first_character_type(pw)

Identifies the type of the first character in a password.

- Returns `digit` if the first character is a number.
- Returns `letter` if the first character is an alphabet.
- Returns `symbol` if the first character is a special character.
- Handles empty or invalid inputs safely.

### 2. split_credentials(text)

Separates a username and password using a colon (`:`) delimiter.

Example:

```python
split_credentials("alice:Secret123")
```

Output:

```python
('alice', 'Secret123')
```

The corrected function also handles malformed credentials and preserves additional colons in the password.

### 3. digit_ratio(pw)

Calculates the proportion of numeric characters in a password.

Formula:

```text
Digit Ratio = Number of Digit Characters / Total Number of Characters
```

Example:

```python
digit_ratio("Pass123")
```

Output:

```text
0.42857142857142855
```

The corrected function safely handles empty and invalid inputs.

---

## Fuzz Testing Using Hypothesis

Hypothesis was used to automatically generate test inputs rather than relying only on manually written test cases.

The tests covered:

- Random strings
- Empty strings
- `None` values
- Unexpected input values
- Edge cases that could cause application crashes

Three test functions were implemented:

| Test Function | Function Tested |
|---|---|
| `test_first_character_type_no_crash()` | `first_character_type()` |
| `test_split_credentials_no_crash()` | `split_credentials()` |
| `test_digit_ratio_no_crash()` | `digit_ratio()` |

Each test used Hypothesis strategies to generate inputs and checked whether the corresponding application function could execute without raising an unexpected exception.

---

## Bugs Identified

The initial fuzz testing identified the following issues:

| Function | Input | Error Identified |
|---|---|---|
| `first_character_type()` | Empty string | `IndexError` |
| `first_character_type()` | `None` | `TypeError` |
| `split_credentials()` | Empty string | `ValueError` |
| `split_credentials()` | `None` | `AttributeError` |
| `digit_ratio()` | Empty string | `ZeroDivisionError` |
| `digit_ratio()` | `None` | `TypeError` |

### Corrections Implemented

- Added input type and empty-string validation.
- Prevented invalid indexing operations.
- Used safer credential splitting with `partition()`.
- Added handling for missing credential separators.
- Prevented division by zero in digit ratio calculations.
- Added appropriate return values for invalid inputs.

---

## Execution and Testing

### 1. Install Dependencies

```bash
pip install hypothesis pytest
```

### 2. Run the Original Application

```bash
python password_policy.py
```

### 3. Execute Fuzz Tests

```bash
python -m pytest test_password_policy.py -v
```

The initial execution identified failures in all three test cases.

### 4. Run the Corrected Application

```bash
python password_policy.py
```

### 5. Re-run the Tests

```bash
python -m pytest test_password_policy.py -v
```

---

## Final Testing Results

After correcting the identified input validation bugs, the Hypothesis test suite was executed again.

| Test Case | Final Status |
|---|---|
| `test_first_character_type_no_crash` | PASSED |
| `test_split_credentials_no_crash` | PASSED |
| `test_digit_ratio_no_crash` | PASSED |
| **Total Tests** | **3 Passed** |

```text
============================= test session starts ==============================

test_password_policy.py::test_first_character_type_no_crash PASSED
test_password_policy.py::test_split_credentials_no_crash PASSED
test_password_policy.py::test_digit_ratio_no_crash PASSED

============================== 3 passed in 0.56s ===============================
```

---

## Learning Outcomes

Through this lab, the following concepts were explored:

- Understanding fuzz testing and its importance in software quality assurance.
- Using Hypothesis for automated property-based testing.
- Identifying unexpected behaviour through automatically generated inputs.
- Understanding common input validation errors and exceptions.
- Applying defensive programming techniques to improve application reliability.
- Using Pytest to verify application correctness after fixing bugs.

---

## Conclusion

This lab demonstrated how fuzz testing can be used to identify input validation bugs that may not be discovered through ordinary testing. Hypothesis successfully identified edge cases in all three functions of the Password Policy Checker, including empty strings and `None` values.

The identified issues were corrected by implementing input validation, safer string processing, and defensive programming techniques. After the modifications, all three Hypothesis tests passed successfully.

The exercise highlighted the importance of automated testing and robust input handling in developing reliable and secure software applications.

---
