from django.urls import path, re_path

from . import views

app_name = "apiv2"

urlpatterns = [
    re_path(r"^", views.v2_not_implemented)
]
