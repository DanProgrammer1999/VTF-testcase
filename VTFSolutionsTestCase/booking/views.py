from rest_framework import status, permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import *


# Create your views here.
class UserView(viewsets.ReadOnlyModelViewSet):
    renderer_classes = [renderers.AdminRenderer]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(detail=False,
            methods=['put'],
            name='Change Password',
            permission_classes=[permissions.IsAuthenticated])
    def change_password(self, request):
        object = request.user
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]},
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            object.set_password(serializer.data.get("new_password"))
            object.save()

            return Response(data={'status': 'password changed'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HotelView(viewsets.ReadOnlyModelViewSet):
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [renderers.AdminRenderer]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Hotel.objects.all()

        return Hotel.objects.filter(admin=user)


class RoomCategoryView(viewsets.ReadOnlyModelViewSet):
    serializer_class = RoomCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [renderers.AdminRenderer]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return RoomCategory.objects.all()

        return RoomCategory.objects.filter(hotel__admin=user)


class RoomView(viewsets.ReadOnlyModelViewSet):
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [renderers.AdminRenderer]

    def get_queryset(self):
        user = self.request.user

        # Filter to allow only user-related rooms (or all for admin)
        all_rooms =              \
            Room.objects.all()   \
            if user.is_superuser \
            else Room.objects.filter(room_category__hotel__admin=user)

        # Filter for room category (if specified)
        category = self.request.query_params.get('room_category', None)
        filtered_rooms =        \
            all_rooms           \
            if category is None \
            else all_rooms.filter(room_category=category)

        return filtered_rooms


class BookingView(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [renderers.AdminRenderer]

    def get_queryset(self):
        user = self.request.user

        # Filter to return only bookings for user-related hotels
        all_bookings =            \
            Booking.objects.all() \
            if user.is_superuser  \
            else Booking.objects.filter(room__room_category__hotel__admin=user)

        # Filter for a room (if specified)
        room = self.request.query_params.get('room', None)
        room_bookings =     \
            all_bookings    \
            if room is None \
            else all_bookings.filter(room=room)

        return room_bookings
