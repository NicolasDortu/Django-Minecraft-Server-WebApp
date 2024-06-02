from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("download/", views.download_file, name="download_file"),
    path("dynmap", views.dynmap_view, name="dynmap"),
    path("mods", views.download_mods),
    path("update", views.download_launcher),
]
