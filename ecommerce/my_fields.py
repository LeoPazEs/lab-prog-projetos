from localflavor.br.models import BRCPFField
from funcionarios.validators.BRCPFField import validate_cpf_numerico


class BRCPFFieldNumeric(BRCPFField):
    """Field para CPF númerico."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(validate_cpf_numerico)
