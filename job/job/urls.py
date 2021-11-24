from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include("home.urls")),
    path("category/", include("category.urls")),
    path("abot_us/", include("about_us.urls")),
    path("users/", include("users.urls")),
    path("", lambda request: redirect("/home/")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)