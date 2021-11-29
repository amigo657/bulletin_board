from django.urls import path
from blog.views import blog_page, blog_details

urlpatterns = [
    path("blog_home/", blog_page, name = "blog_home"),
    path("blog_details/", blog_details, name = "blog_details")
]

