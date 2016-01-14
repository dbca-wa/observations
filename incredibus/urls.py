from django.conf.urls import patterns, include, url

from weather.views import index, weatherstation
from weather.models import v1_api
from weather.admin import site

urlpatterns = patterns('',
    url(r'^admin/', include(site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^$', index),
    url(r'^station/(?P<station>\d+)$', weatherstation)
)
