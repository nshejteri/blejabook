from django.conf.urls import patterns, include, url
from userprofile import views

urlpatterns = patterns('',
	url(r'^profile/(?P<username>[\w\-]+)/$', views.user_profile, name='user_profile'),
	url(r'^edit_profile/(?P<username>[\w\-]+)/$', views.edit_profile, name='edit_profile'),
)