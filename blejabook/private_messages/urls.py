from django.conf.urls import patterns, url
from private_messages import views


urlpatterns = patterns('',
	url(r'^$', views.user_threads, name='user_threads'),
	url(r'^compose_message/(?P<username>[\w\-]+)/$', views.compose_message, name='compose_message'),
	url(r'^message/(?P<thread_id>[0-9]+)/$', views.thread_messages, name='thread_messages'),
	url(r'^delete/(?P<thread_id>[0-9]+)/(?P<last_msg_id>[0-9]+)$', views.delete_thread, name='delete_thread'),
)
