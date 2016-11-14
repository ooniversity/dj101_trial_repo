from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.list_view, name='list_view'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
]
