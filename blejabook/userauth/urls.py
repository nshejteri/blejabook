from django.conf.urls import patterns, url
from userauth import views

urlpatterns = patterns('',

	url(r'^signup/$', views.signup, name='account_signup')
)