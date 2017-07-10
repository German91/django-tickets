"""
Ticket Urls
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ticket_list, name='ticket_list'),
    url(r'^create/$', views.ticket_create, name='ticket_create'),
    url(r'^edit/(?P<slug>[-\w]+)/$', views.ticket_edit, name='ticket_edit'),
    url(r'^delete/$', views.ticket_delete, name="ticket_delete"),
]
