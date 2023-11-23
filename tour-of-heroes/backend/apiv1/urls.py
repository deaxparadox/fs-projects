from django.urls import path, include, re_path

from . import views

app_name = 'apiv1'

urlpatterns = [
    path("heroes/", views.get_heroes, name="api_get_heroes"),
    path("heroes/<int:id>/", views.get_hero, name="api_get_hero"),
    path("heroes/create/", views.add_hero, name="api_create_hero"),
]

