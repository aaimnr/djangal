from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^djang/', include('djangal.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',
	        {'document_root': '/Users/am/short/dj/media'}),
	(r'^dywan/(?P<dywan_id>\d+)/$', 'djangal.galeria.views.dywan'),
	(r'^album/(?P<album_id>\d+)/$', 'djangal.galeria.views.album'),
	(r'^albumy/$', 'djangal.galeria.views.albumy'),
)
