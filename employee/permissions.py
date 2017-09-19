from rest_framework import permissions
from rest_framework import authentication
from account.models import *
from employee.models import *


class TeamPermission(permissions.IsAuthenticated):


    def has_object_permission(self, request, view, obj):
        if obj.lead== request.user or request.user.is_superuser:
            return True
        else:
            if request.method in ('HEAD', 'OPTIONS', 'GET'):
                return True
            return False

class ProjectPermission(permissions.IsAuthenticated):


    def has_object_permission(self, request, view, obj):
        if obj.team.lead== request.user or request.user.is_superuser:
            return True
        else:
            if request.method in ('HEAD', 'OPTIONS', 'GET'):
                return True
            return False

class TaskPermission(permissions.IsAuthenticated):


    def has_object_permission(self, request, view, obj):
        if obj.project.team.lead== request.user or request.user.is_superuser:
            return True
        else:
            if request.method in ('HEAD', 'OPTIONS', 'GET'):
                return True
            return False