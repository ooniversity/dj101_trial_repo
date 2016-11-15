
from django.contrib import admin
from courses.models import Course, Lesson
from django.forms import widgets
from coaches.models import Coach
# -*- coding: utf-8 -*-
class LessonInline(admin.TabularInline):
    extra = 0
    model = Lesson
    fields = ['subject', 'description', 'order']
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name',  'short_description']
    search_fields = ['name']
    inlines = [LessonInline]

    




admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
