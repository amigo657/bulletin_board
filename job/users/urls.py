from django.urls import path
# from users.views import login, logout
from django.shortcuts import redirect

urlpatterns = [
    # path("login/", login, name = "log_in"),
    # path("logout/", logout, name = "log_out"),
    path("", lambda request: redirect("/users/login")),
]
