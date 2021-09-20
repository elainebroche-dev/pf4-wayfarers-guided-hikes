from . import views
from django.urls import path

urlpatterns = [
    path("", views.HikeList.as_view(), name="home"),
    path('<slug:slug>/', views.HikeDetail.as_view(), name='hike_detail'),
    path('like/<slug:slug>', views.HikeLike.as_view(), name='hike_like'),
]