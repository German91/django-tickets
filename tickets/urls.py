from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ticket_list, name='ticket_list'),
    url(r'^create/$', views.ticket_create, name='ticket_create'),
    url(r'^edit/(?P<pk>\d+)/$', views.ticket_edit, name='ticket_edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.ticket_delete, name="ticket_delete"),
]
