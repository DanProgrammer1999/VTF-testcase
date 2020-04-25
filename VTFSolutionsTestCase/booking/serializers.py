from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ['url', 'first_name', 'last_name', 'username', 'email', 'password']


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ['url', 'name', 'admin', 'room_categories']


class RoomCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoomCategory
        fields = ['url', 'name', 'min_price', 'hotel', 'total_count', 'rooms']


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ['url', 'name', 'room_category']


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['url', 'room', 'check in date', 'check out date']
