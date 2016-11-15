from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentModelForm
from django.contrib import messages
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import logging
logger = logging.getLogger(__name__)


class StudentDetailView(DetailView):
    model = Student
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        logger.debug("Students detail view has been debugged")
        logger.info("Logger of students detail view informs you!")
        logger.warning("Logger of students detail view warns you!")
        logger.error("Students detail view went wrong!")
        return context


class StudentListView(ListView):
    model = Student
    fields = "__all__"    
    paginate_by = 2
    
    def get_queryset(self):
        if 'course_id' in self.request.GET:
            student_list = Student.objects.filter(courses=self.request.GET['course_id'])
            #paginator = Paginator(student_list, 2)
            #page = self.request.GET.get('page')
            #try:
              #  contacts = paginator.page(page)
           # except PageNotAnInteger:
        # If page is not an integer, deliver first page.
               # contacts = paginator.page(1)
            #except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
                #contacts = paginator.page(paginator.num_pages)
        else:
            student_list = Student.objects.all()
            #paginator = Paginator(student_list, 2)
            #page = self.request.GET.get('page')
            #try:
            #    contacts = paginator.page(page)
            #except PageNotAnInteger:
        # If page is not an integer, deliver first page.
               # contacts = paginator.page(1)
           # except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
               # contacts = paginator.page(paginator.num_pages)
        return student_list
    
class StudentCreateView(CreateView):
    model = Student
    fields = "__all__"    
    success_url = reverse_lazy('students:list_view')
    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Student %s %s has been successfully added.' % (
                form.instance.name, form.instance.surname))
        return super(StudentCreateView, self).form_valid(form)        
                
class StudentUpdateView(UpdateView):
    model = Student
    fields = "__all__"    
    def get_success_url(self, **kwargs):
        return reverse_lazy('students:edit', args=(self.object.pk,))
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context
    def form_valid(self, form):
        
        messages.success(self.request, 'Info on the student has been successfully changed.')
        return super(StudentUpdateView, self).form_valid(form)
                  
class StudentDeleteView(DeleteView):
    model = Student
    fields = "__all__"    
    success_url = reverse_lazy('students:list_view')
    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context
    def delete(self, request, *args, **kwargs):
        stud = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (
                self.object.name, self.object.surname))
        return stud
        

        
