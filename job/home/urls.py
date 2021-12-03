from django.urls import path
from home.views import home_page
# from home.views import link_em

urlpatterns = [
    # path("link", link_em,  name = "home"),
    path("", home_page, name = "home"),
]
