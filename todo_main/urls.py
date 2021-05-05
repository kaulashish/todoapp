from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", list, name="home"),
    path("<int:pk>/edit", update, name="update"),
    path("<int:pk>/delete", delete, name="delete"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("signup/", Signup.as_view(), name="signup"),
]
