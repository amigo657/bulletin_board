from django.urls import path
from users.views import login, logout, signin
from django.shortcuts import redirect

urlpatterns = [
    path("login/", login, name = "log_in"),
    path("logout/", logout, name = "log_out"),
    path("sign_in/", signin, name = "sign_in"),
    path("", lambda request: redirect("/users/login")),
]
