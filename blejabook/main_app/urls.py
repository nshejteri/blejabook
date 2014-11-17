from django.conf.urls import url, patterns
from main_app import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^profile/(?P<username>[\w\-]+)/$', views.user_profile, name='user_profile'),
)