from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ticket_list, name='ticket_list'),
    url(r'^create/$', views.ticket_create, name='ticket_create'),
]
