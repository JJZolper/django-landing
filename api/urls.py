from django.urls import path, include, re_path
from . import views as api

urlpatterns = [
    path('register/', api.CreateUserAPI.as_view(), name="create_user"),
]