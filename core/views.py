from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .forms import LoginForm, UserForm


class RegisterView(SuccessMessageMixin, FormView):

    template_name = "registration.html"
    form_class = UserForm
    success_url = reverse_lazy("login")
    success_message = "Cadastro realizado com sucesso."

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data["username"],
            email=form.cleaned_data["email"],
            password=form.cleaned_data["password"],
        )
        return super().form_valid(form)


class UserLoginView(SuccessMessageMixin, LoginView):

    template_name = "login.html"
    form_class = LoginForm
    redirect_authenticated_user = True
    next_page = reverse_lazy("list-cars")
    success_message = "Login realizado com sucesso."

class UserLogoutView(LogoutView):
    next_page = reverse_lazy("login")
