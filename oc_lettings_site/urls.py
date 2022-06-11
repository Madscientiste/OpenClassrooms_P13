from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sentry-debug/", views.sentry_debug, name="sentry_debug"),
    path("admin/", admin.site.urls),
    path("lettings/", include("lettings.urls"), name="lettings"),
    path("profiles/", include("profiles.urls"), name="profiles"),
]
