from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserForm(forms.ModelForm):
    """ Form used to register user."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    password = forms.CharField(widget=forms.PasswordInput(), label="Sua senha")

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        labels = {
            "username": "Seu usuário",
            "email": "Seu email",
            "password": "Sua senha",
        }


class LoginForm(AuthenticationForm):
    """ Form used to login user. """

    def __init__(self, *args,  request=None, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    username = forms.CharField(label="Seu Usuário")
    password = forms.CharField(
        label="Sua senha",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
