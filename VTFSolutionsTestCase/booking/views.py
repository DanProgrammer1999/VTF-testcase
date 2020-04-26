from rest_framework import status, permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import *


# Create your views here.
class UserView(viewsets.ModelViewSet):
    renderer_classes = [renderers.AdminRenderer]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(detail=False,
            methods=['put', 'get'],
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


class HotelView(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAdminUser]
    renderer_classes = [renderers.AdminRenderer]

    def create(self, request, pk=None, *args, **kwargs):
        data = request.data.copy()
        data['pk'] = pk
        serializer = HotelSerializer(data=data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomCategoryView(viewsets.ModelViewSet):
    serializer_class = RoomCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return RoomCategory.objects.filter(hotel__admin=user)


class RoomView(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Room.objects.filter(room_category__hotel__admin=user)


class BookingView(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Booking.objects.filter(room__room_category__hotel__admin=user)
