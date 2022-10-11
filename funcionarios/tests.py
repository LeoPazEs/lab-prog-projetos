from datetime import timedelta
from django.utils import timezone
from django.test import TestCase
from django.core.exceptions import ValidationError
from funcionarios.validators.datefield import validate_lt_date
from funcionarios.validators.BRCPFField import validate_cpf_numerico


class TestValidacoesDosModels(TestCase):
    """Test dos validadores dos models."""
    def test_data_nascimento_validator(self):
        """Teste de validação de data de nascimento."""
        with self.assertRaises(ValidationError):
            validate_lt_date(timezone.now().date() + timedelta(days=1))

        validate_lt_date(timezone.now().date())

    def test_cpf_numerico_validator(self):
        """Teste de validação do CPF."""
        with self.assertRaises(ValidationError):
            validate_cpf_numerico("121.978.294-75")

        validate_cpf_numerico("12197829475")
