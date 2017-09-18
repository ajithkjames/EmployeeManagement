# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from employee.models import Team, Project, Task

admin.site.register(Team)
admin.site.register(Project)
admin.site.register(Task)
