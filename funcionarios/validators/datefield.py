from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_lt_date(value):
    """Valida se a data de nascimento é menor que ou igual a data atual"""
    if timezone.now().date() < value:
        raise ValidationError("Data de nascimento inválida.")
    return value
