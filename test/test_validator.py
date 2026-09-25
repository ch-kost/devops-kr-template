# tests/test_validator.py
from validator import validate_email, validate_snils


def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False


def test_validate_snils():
    # Валидные СНИЛС (рассчитаны по алгоритму)
    assert validate_snils("11223344595") == True
    assert validate_snils("001-001-999 65") == True  # с форматированием

    # Невалидные: неверный формат
    assert validate_snils("123") == False              # слишком короткий
    assert validate_snils("123456789012") == False     # слишком длинный
    assert validate_snils("abcdefghijk") == False      # не цифры

    # Невалидные: неверная контрольная сумма
    assert validate_snils("11223344500") == False
