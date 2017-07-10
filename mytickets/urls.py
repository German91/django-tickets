from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from authentication.views import register, change_password

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', register, name='register'),
    url(r'^tickets/', include('tickets.urls')),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^$', views.login, name='login', kwargs={'redirect_authenticated_user': True}),
    url(r'^accounts/', include('authentication.urls')),
    url(r'^accounts/change-password', change_password, name='change-password'),
]
