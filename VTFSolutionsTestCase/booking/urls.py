from rest_framework import routers
from django.urls import include, path
from .views import *

router = routers.DefaultRouter()
router.register('users', UserView)
router.register('hotels', HotelView)
router.register('room_categories', RoomCategoryView)
router.register('rooms', RoomView, basename='room')
router.register('bookings', BookingView)

urlpatterns = [
    path('', include(router.urls))
]
