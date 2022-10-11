from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def cpf_formatter(value):
    """ Tag para formatar CPF na template."""
    return f"{value[:3]}.{value[3:6]}.{value[6:9]}-{value[9:]}"
