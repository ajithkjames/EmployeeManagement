# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from account.models import User, Skill
from employee.models import Team, Project, Task
from employee.serializers import TeamSerializer, ProjectSerializer, TaskSerializer, ProjectCreateSerializer, TeamCreateSerializer, TaskCreateSerializer
from employee.permissions import TeamPermission, ProjectPermission, TaskPermission



class TaskViewSet(viewsets.ModelViewSet):
	"""Tasks API view"""

	serializer_class = TaskSerializer
	queryset = Task.objects.all()
	permission_classes = (TaskPermission,)

	def get_serializer_class(self):
		if self.request.method != 'GET': 
			self.serializer_class = TaskCreateSerializer 
		return self.serializer_class


class TeamViewSet(viewsets.ModelViewSet):
	"""Team API view"""

	serializer_class = TeamSerializer
	queryset = Team.objects.all()
	permission_classes = (TeamPermission,)

	def get_serializer_class(self):
		print self.request
		if self.request.method != 'GET': 
			self.serializer_class = TeamCreateSerializer 
		return self.serializer_class


class ProjectViewSet(viewsets.ModelViewSet):
	"""Project API view"""

	serializer_class = ProjectSerializer
	queryset = Project.objects.all()
	permission_classes = (ProjectPermission,)

	def get_serializer_class(self):
		if self.request.method != 'GET': 
			self.serializer_class = ProjectCreateSerializer 
		return self.serializer_class


class EmployeeTasks(generics.ListAPIView):
	"""Employee's assigned tasks API view"""
	
	serializer_class = TaskSerializer

	def get_queryset(self):
	    return Task.objects.filter(assignee=self.request.user)
