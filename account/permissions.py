from rest_framework import permissions
from rest_framework import authentication
from account.models import *


class UserPermissions(permissions.IsAuthenticated):

    def has_permission(self, request, view):

        if request.user.is_authenticated:
            return True
        if request.method in ('HEAD', 'OPTIONS', 'POST'):
            return True

    def has_object_permission(self, request, view, obj):
        if obj== request.user or request.user.is_superuser:
            return True