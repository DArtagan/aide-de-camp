from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^accounts/login/', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('authtools.urls')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^companies/', include('companies.urls', namespace="company")),
    url(r'^questions/', include('questions.urls', namespace="question")),
)
