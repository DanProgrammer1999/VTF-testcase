from rest_framework import generics, permissions, viewsets
from .serializers import *


# Create your views here.
class UserList(generics.ListAPIView, viewsets.ViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserDetail(generics.RetrieveUpdateAPIView, viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class HotelList(generics.ListAPIView, viewsets.ViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAdminUser]


class HotelDetail(generics.RetrieveUpdateAPIView, viewsets.ViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAdminUser]


class RoomCategoryList(generics.ListAPIView, viewsets.ViewSet):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return RoomCategory.objects.filter(hotel__admin=user)


class RoomCategoryDetail(generics.RetrieveAPIView, viewsets.ViewSet):
    serializer_class = RoomCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = RoomCategory.objects.all()


class RoomList(generics.ListAPIView, viewsets.ViewSet):
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Room.objects.filter(room_category__hotel__admin=user)


class RoomDetail(generics.RetrieveAPIView, viewsets.ViewSet):
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Room.objects.all()


class BookingList(generics.ListAPIView, viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Booking.objects.filter(room__room_category__hotel__admin=user)
