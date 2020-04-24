from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class Hotel(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name', 'admin']


class RoomCategory(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoomCategory
        fields = ['name', 'min_price', 'hotel', 'total_count']


class Room(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ['name', 'room_category']


class Booking(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['room', 'date_check_in', 'date_check_out']

