from django.conf.urls import patterns, url
from userauth import views

urlpatterns = patterns('',
	url(r'^signup/$', views.signup, name='account_signup'),
	url(r'^login/$', views.user_login, name='user_login'),
	url(r'^logout/$', views.user_logout, name='user_logout'),
	url(r'^confirm_email/(\w+)/$', views.confirm_email),
)