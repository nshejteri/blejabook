from django.conf.urls import patterns, url
from private_messages import views


urlpatterns = patterns('',
	url(r'^$', views.user_messages, name='user_messages'),
	url(r'^compose_message/(?P<username>[\w\-]+)/$', views.compose_message, name='compose_message'),
)
