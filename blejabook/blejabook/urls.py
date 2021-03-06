from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blejabook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('main_app.urls')),
    url(r'^accounts/', include('userprofile.urls')),
    url(r'^account/', include('userauth.urls')),
    url(r'^messages/', include('private_messages.urls'))
)
