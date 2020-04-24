from rest_framework import permissions


class HotelOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(view)
        return True
