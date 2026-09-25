# validator.py
def validate_email(email: str) -> bool:
    """Валидация email-адреса."""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Проверка российского номера: +7 или 7 и ещё десять цифр."""
    import re

    normalized = phone.replace(' ', '').replace('-', '')
    return bool(re.fullmatch(r'\+?7\d{10}', normalized))

