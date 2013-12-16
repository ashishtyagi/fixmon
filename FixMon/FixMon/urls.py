from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
#from django.conf.urls.default import *

# Uncomment the next two lines to enable the admin:
from tastypie.api import Api
from fixmon.api import FixMsgResource, ColumnConfigResource
from django.contrib import admin
admin.autodiscover()


v1_api = Api(api_name='v1')
v1_api.register(FixMsgResource())
v1_api.register(ColumnConfigResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FixMon.views.home', name='home'),
    # url(r'^FixMon/', include('FixMon.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', RedirectView.as_view(url='static/index.html', permanent=False), name='index'),
    url(r'^index.html$', RedirectView.as_view(url='static/index.html', permanent=False), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
