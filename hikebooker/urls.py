from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.HikeList.as_view(), name="home"),
    path('detail/<slug:slug>', views.HikeDetail.as_view(), name='hike_detail'),
    path('like/<slug:slug>', login_required(views.HikeLike.as_view()), name='hike_like'),
    path('book', login_required(views.HikeBook.as_view()), name='hike_book'),
    path('bookings', login_required(views.HikeMyBookings.as_view()), name='hike_mybookings'),
]
