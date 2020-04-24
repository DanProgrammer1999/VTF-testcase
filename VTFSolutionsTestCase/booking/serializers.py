from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    admin = UserSerializer()

    class Meta:
        model = Hotel
        fields = ['name', 'admin']

    def create(self, validated_data):
        hotel = Hotel(name=validated_data['name'], admin=validated_data['admin'])
        print(hotel)
        hotel.save()


class RoomCategorySerializer(serializers.HyperlinkedModelSerializer):
    hotel = HotelSerializer()

    class Meta:
        model = RoomCategory
        fields = ['name', 'min_price', 'hotel', 'total_count']


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    room_category = RoomCategorySerializer()

    class Meta:
        model = Room
        fields = ['name', 'room_category']


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['room', 'date_check_in', 'date_check_out']
