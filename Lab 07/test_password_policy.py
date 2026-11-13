
from hypothesis import given, strategies as st, settings
from password_policy import (
    first_character_type,
    split_credentials,
    digit_ratio
)

# Test 1: first_character_type
@given(st.one_of(st.text(), st.none()))
@settings(max_examples=100)
def test_first_character_type_no_crash(s):
    try:
        first_character_type(s)
    except Exception as e:
        assert False, f"first_character_type crashed with input {s!r}: {e}"


# Test 2: split_credentials
@given(st.one_of(st.text(), st.none()))
@settings(max_examples=100)
def test_split_credentials_no_crash(s):
    try:
        split_credentials(s)
    except Exception as e:
        assert False, f"split_credentials crashed with input {s!r}: {e}"


# Test 3: digit_ratio
@given(st.one_of(st.text(), st.none()))
@settings(max_examples=100)
def test_digit_ratio_no_crash(s):
    try:
        digit_ratio(s)
    except Exception as e:
        assert False, f"digit_ratio crashed with input {s!r}: {e}"
