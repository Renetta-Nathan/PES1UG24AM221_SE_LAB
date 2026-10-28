
from password_policy import check_password, strength, suggest_fix


def test_valid_password():
    assert check_password("Abcdef1!") == []


def test_password_too_short():
    assert "too short" in check_password("Ab1!")


def test_password_too_long():
    password = "Abcdef1!" + "x" * 60
    assert "too long" in check_password(password)


def test_common_password():
    assert "common" in check_password("password")


def test_missing_uppercase():
    assert "no uppercase" in check_password("abcdef1!")


def test_missing_lowercase():
    assert "no lowercase" in check_password("ABCDEFG1!")


def test_missing_digit():
    assert "no digit" in check_password("Abcdefgh!")


def test_missing_special_character():
    assert "no special" in check_password("Abcdefg1")


def test_strong_password():
    assert strength("Abcdefghij1!XYZ") == "strong"


def test_good_password():
    assert strength("Abcdef1!") == "good"


def test_weak_password():
    assert strength("Abcdefgh1") == "weak"


def test_very_weak_password():
    assert strength("") == "very weak"


def test_suggest_fix_for_short_password():
    assert suggest_fix(["too short"]) == "add more characters"


def test_suggest_fix_for_common_password():
    assert suggest_fix(["common"]) == "avoid common passwords"


def test_suggest_fix_for_missing_character():
    assert suggest_fix(["no digit"]) == "add digit"


def test_suggest_fix_for_other_issue():
    assert suggest_fix(["too long"]) == "shorten it"


def test_no_fix_needed():
    assert suggest_fix([]) == "none needed"
