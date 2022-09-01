from django.urls import path, include 
from .views import list_carros, detalhe_carros

urlpatterns = [ 
    path("", list_carros, name= "list_carros"),
    path("<int:id>/", detalhe_carros, name= "detalhe_carro")
]
