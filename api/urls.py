from django.urls import path, include, re_path
from . import views as api

urlpatterns = [
    path('register/', api.create_user, name="create_user"),
]