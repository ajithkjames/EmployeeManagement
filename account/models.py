# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models


class Skill(models.Model):
    """skills model"""

    name = models.CharField(max_length=50)

    def __str__(self):
        return u'%s' % (self.name)


class User(AbstractUser):
    """user model"""

    age = models.PositiveIntegerField(null=True, blank=True)
    empid = models.CharField(max_length=255, blank=True, null=True, unique=True)
    teamlead = models.BooleanField(default=False, verbose_name="Team Lead")
    skills = models.ManyToManyField(Skill, related_name="skills" )



