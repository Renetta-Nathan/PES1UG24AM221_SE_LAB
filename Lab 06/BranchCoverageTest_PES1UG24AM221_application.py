
from password_policy import check_password, strength, suggest_fix


def test_length_branches():
    assert "too short" in check_password("Ab1!")
    assert check_password("Abcdef1!") == []
    assert "too long" in check_password("Abcdef1!" + "x" * 60)


def test_common_password_branches():
    assert "common" in check_password("password")
    assert "common" not in check_password("Abcdef1!")


def test_character_type_branches():
    assert check_password("Abcdef1!") == []
    assert "no uppercase" in check_password("abcdef1!")
    assert "no lowercase" in check_password("ABCDEFG1!")
    assert "no digit" in check_password("Abcdefgh!")
    assert "no special" in check_password("Abcdefg1")


def test_strength_branches():
    assert strength("Abcdefghij1!XYZ") == "strong"
    assert strength("Abcdef1!") == "good"
    assert strength("Abcdefgh1") == "weak"
    assert strength("") == "very weak"


def test_suggest_fix_empty_issues():
    assert suggest_fix([]) == "none needed"


def test_suggest_fix_too_short():
    assert suggest_fix(["too short"]) == "add more characters"


def test_suggest_fix_common():
    assert suggest_fix(["common"]) == "avoid common passwords"


def test_suggest_fix_missing_character():
    assert suggest_fix(["no uppercase"]) == "add uppercase"
    assert suggest_fix(["no lowercase"]) == "add lowercase"
    assert suggest_fix(["no digit"]) == "add digit"
    assert suggest_fix(["no special"]) == "add special"


def test_suggest_fix_fallback():
    assert suggest_fix(["too long"]) == "shorten it"
