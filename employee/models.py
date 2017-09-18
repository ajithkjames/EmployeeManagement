# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from account.models import User,Skill


class Team(models.Model):
	"""Team Model"""

	name = models.CharField(max_length=50)
	lead= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	members = models.ManyToManyField(User, related_name='team_members' )

	def __str__(self):
		return u'%s - %s' % (self.name, self.lead)


class Project(models.Model):
	"""Project Model"""

	name = models.CharField(max_length=50)
	team= models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE)
	members= models.ManyToManyField(User)

	def __str__(self):
		return u'%s - %s' % (self.team.name, self.name)


class Task(models.Model):
	"""Tasks Model"""
	
	title = models.CharField(max_length=50)
	content = models.TextField()
	assignee = models.ForeignKey(User, null=True, blank=True)
	project = models.ForeignKey(Project, null=True, blank=True)

	def __str__(self):
		return u'%s - %s' % (self.project, self.title)