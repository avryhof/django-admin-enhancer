from __future__ import unicode_literals

from django.conf.urls import include, url

from .admin import site


urlpatterns = [
    url(r'^admin/', include(site.urls)),
]
