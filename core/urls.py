from django.urls import path, include, re_path
from core import views as core

urlpatterns = [
    path('', core.HomeView.as_view(), name="home"),
]