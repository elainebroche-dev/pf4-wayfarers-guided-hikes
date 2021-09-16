from . import views
from django.urls import path

urlpatterns = [
    path("", views.HikeList.as_view(), name="home"),
]