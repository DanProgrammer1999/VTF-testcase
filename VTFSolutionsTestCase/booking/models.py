from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# For user model, I will use predefined django User model


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RoomCategory(models.Model):
    name = models.CharField(max_length=100)
    min_price = models.FloatField()
    hotel = models.ForeignKey(Hotel, related_name='room_categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=100)
    room_category = models.ForeignKey(RoomCategory, related_name='rooms', on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.name, self.room_category.name)


class Booking(models.Model):
    room = models.ForeignKey(Room, related_name='room_bookings', on_delete=models.CASCADE)
    date_check_in = models.DateField()
    date_check_out = models.DateField()

    def __str__(self):
        return "{} ({}) from {} to {}".format(self.room.name, self.room.room_category.name, self.date_check_in, self.date_check_out)
