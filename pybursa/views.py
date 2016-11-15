from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from courses.models import Course


def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})


def contact(request):
    return render(request, 'contact.html')


# def handler404(request):  # handler404 not_found
#     response = render_to_response('404.html', { 'message' : 'Sorry, page is not found' },
#                                   context_instance=RequestContext(request))
#     response.status_code = 404
#     return response
#
#
# def handler500(request):  # handler500 server_error
#     response = render_to_response('500.html', { 'message' : 'Sorry, internal server error occurred' },
#                                   context_instance=RequestContext(request))
#     response.status_code = 500
#     return response

