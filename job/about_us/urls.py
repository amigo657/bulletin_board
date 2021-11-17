from django.urls import path
from about_us.views import about

urlpatterns = [
    path("", about, name = "about")
]
