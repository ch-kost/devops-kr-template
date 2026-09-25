from validator import validate_phone


def test_validate_phone():
    assert validate_phone("+7 900-123-45-67") is True
    assert validate_phone("7-900-123-45-67") is True
    assert validate_phone("8 900 123 45 67") is False
    assert validate_phone("9001234567") is False
    assert validate_phone("+7 abc") is False
