from django.views.generic import ListView
from .models import Departamento


class DepartamentoListView(ListView):
    """View que lista os departamentos e seus respectivos funcionarios."""

    queryset = Departamento.objects.all().prefetch_related('funcionarios')
    template_name = "list_funcionario.html"
