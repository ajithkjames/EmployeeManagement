# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from account.models import User, Skill
from employee.models import Team, Project, Task
from employee.serializers import TeamSerializer, ProjectSerializer, TaskSerializer
from employee.permissions import TeamPermission, ProjectPermission, TaskPermission



class TaskViewSet(viewsets.ModelViewSet):
	"""Tasks API view"""

	serializer_class = TaskSerializer
	queryset = Task.objects.all()
	permission_classes = (TaskPermission,)



class TeamViewSet(viewsets.ModelViewSet):
	"""Team API view"""

	serializer_class = TeamSerializer
	queryset = Team.objects.all()
	permission_classes = (TeamPermission,)



class ProjectViewSet(viewsets.ModelViewSet):
	"""Project API view"""

	serializer_class = ProjectSerializer
	queryset = Project.objects.all()
	permission_classes = (ProjectPermission,)



class EmployeeTasks(generics.ListAPIView):
	"""Employee's assigned tasks API view"""
	
	serializer_class = TaskSerializer

	def get_queryset(self):
	    return Task.objects.filter(assignee=self.request.user)
