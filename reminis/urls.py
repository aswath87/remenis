from django.conf.urls import patterns, include, url
from reminis.core import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from reminis import settings

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
                      
    url(r'^$', views.home),
    url(r'^home/$', views.home),
    url(r'^post/$', views.post),
    url(r'^search/$', views.search),
    
    url(r'^logout/$', views.logout),
    (r'^xd_receiver\.html$', views.xd_receiver),
    
    (r'^facebook/', include('django_facebook.urls')),
)

urlpatterns += staticfiles_urlpatterns()

admin.autodiscover()

if not settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)