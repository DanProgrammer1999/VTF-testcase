from rest_framework import routers
from django.urls import include, path
from .views import *

router = routers.DefaultRouter()
router.register('users', UserList)
router.register('user_detail', UserDetail)
router.register('hotels', HotelList)
router.register('hotel_detail', HotelDetail)
router.register('room_categories', RoomCategoryList)
router.register('room_category_detail', RoomCategoryDetail)
router.register('rooms', RoomList, basename='room')
router.register('room_detail', RoomDetail)
router.register('bookings', BookingList)

urlpatterns = [
    path('', include(router.urls))
]
