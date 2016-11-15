# -*- coding: utf-8 -*-

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Student


class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list')

    def form_valid(self, form):
        super_valid = super(StudentCreateView, self).form_valid(form)
        messages.success(self.request,
                         'Student {} {} has been successfully added.'.format(self.object.name, self.object.surname))
        return super_valid

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context.update({
            "title": 'New student'
        })
        return context


class StudentUpdateView(UpdateView):
    model = Student
    success_url = '/students/edit/%(id)d/'

    def form_valid(self, form):
        messages.success(self.request, 'Info on the student has been sucessfully changed.')
        return super(StudentUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context.update({
            "title": 'Edit student data'
        })
        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')

    def delete(self, request, *args, **kwargs):
        delete_super = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request,
                         'Info on {} {} has been sucessfully deleted.'.
                         format(self.object.name, self.object.surname))
        return delete_super
