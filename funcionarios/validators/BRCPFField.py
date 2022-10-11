from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_cpf_numerico(value):
    """Valida se o CPF é numerico."""
    if not value.isnumeric():
        raise ValidationError("CPF apenas números.")
    return value
