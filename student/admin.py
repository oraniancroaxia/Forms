# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Detail
from .models import Course
from .models import Subject

class StudentAdmin(admin.ModelAdmin):
	fieldset = [("Student Detail", {"field":["first_name","last_name"]})
	]

def Student_Course(self,obj):
	return obj.list_course()

list_display = ("first_name","last_name")

admin.site.register(Detail)
admin.site.register(Course)
admin.site.register(Subject)

# Register your models here.
