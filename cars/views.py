from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Car


class CarListView(LoginRequiredMixin, ListView):
    model = Car
    template_name = "list_cars.html"
    context_object_name = "obj_list"
    login_url = reverse_lazy("login")


class CarDetailView(LoginRequiredMixin, DetailView):
    model = Car
    template_name = "detail_cars.html"
    login_url = reverse_lazy("login")
