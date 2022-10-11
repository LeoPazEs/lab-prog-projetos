from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from ecommerce.my_fields import BRCPFFieldNumeric
from .validators.datefield import validate_lt_date

ESTADOS_CIVIS = [
    ("S", "Solteiro"),
    ("C", "Casado"),
    ("D", "Divorciado"),
    ("V", "Viúvo"),
]

# Create your models here.
class Funcionario(models.Model):
    """Model dos funcionários da empresa."""

    nome = models.CharField(max_length=200)
    salario = models.FloatField(validators=[MinValueValidator(0.0)])
    cpf = BRCPFFieldNumeric("CPF")

    def __str__(self) -> str:
        return f"{self.nome}"


class Perfil(models.Model):
    """Model dos perfis dos funcionário."""

    funcionario = models.OneToOneField(
        Funcionario, on_delete=models.CASCADE, primary_key=True
    )
    nome_social = models.CharField(max_length=200)
    estado_civil = models.CharField(max_length=1, choices=ESTADOS_CIVIS)
    data_nascimento = models.DateField(validators=[validate_lt_date])

    @property
    def idade(self) -> int:
        return timezone.now().year - self.data_nascimento.year

    def __str__(self) -> str:
        return f"{self.nome_social}"


class Departamento(models.Model):
    """Modelo dos departamentos dos funcionários."""

    nome = models.CharField(max_length=200)
    funcionarios = models.ManyToManyField(Funcionario, related_name="funcionarios")
    descricao = models.CharField("Descrição", max_length=500)

    def __str__(self) -> str:
        return f"{self.nome}"
