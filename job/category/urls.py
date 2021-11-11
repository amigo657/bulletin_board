from django.urls import path
from category.views import category_page

urlpatterns = [
    path("", category_page, name = "category")
]
