from django.contrib import admin
from .models import Student
# -*- coding: utf-8 -*-
class StudentAdmin(admin.ModelAdmin):
    def full_name(self, obstud):
        return '%s %s' % (obstud.name, obstud.surname)
    list_display = ['full_name',  'email', 'skype']
    search_fields = ['surname', 'email']
    list_filter=['courses']
    fieldsets = (
        ('Personal info', {
            'fields': ('name', 'surname', 'date_of_birth')
        }),
        ('Contact info', {
            
            'fields': ('email', 'phone', 'address', 'skype')
        }),
        (None, {
            
            'fields': ('courses',)
        }),)
    
admin.site.register(Student, StudentAdmin)
