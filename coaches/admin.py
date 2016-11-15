from django.contrib import admin
from .models import Coach
from django.contrib.admin import BooleanFieldListFilter
from django.contrib.auth.models import User

class CoachAdmin(admin.ModelAdmin):
    list_display = ['first_name',  'last_name', 'gender', 'skype', 'description']
    
    list_filter = (
        ('user__is_staff', BooleanFieldListFilter),
    )




admin.site.register(Coach, CoachAdmin)
# Register your models here.
