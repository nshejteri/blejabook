from django.conf.urls import patterns, url
from userauth import views

urlpatterns = patterns('',
	url(r'^signup/$', views.signup, name='account_signup'),
	url(r'^login/$', views.user_login, name='user_login'),
	url(r'^logout/$', views.user_logout, name='user_logout'),
	url(r'^confirm_email/(\w+)/$', views.confirm_email),
	url(r'^password/reset/$', 'django.contrib.auth.views.password_reset', name="password_reset"),
	url(r'^password/reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
	url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
	url(r'^password/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
)