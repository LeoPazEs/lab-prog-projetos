from django.urls import path
from .views import RegisterView, UserLoginView, UserLogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('', UserLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
]
