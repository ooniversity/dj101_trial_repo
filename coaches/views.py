from django.shortcuts import render
from .models import Coach
from courses.models import Course

def detail(request, pk):
    return render(request, 'coaches/detail.html', { 'coach' : Coach.objects.get(id=pk), 'course_coach' : Course.objects.filter(coach=pk), 'course_assistant' : Course.objects.filter(assistant=pk)})
# Create your views here.

