from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path("heroes/", views.get_heroes, name="api_get_heroes"),
    path("heroes/<int:id>/", views.get_hero, name="api_get_hero"),
]
