# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User, Skill

class CustomUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('age','skills')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Skill)