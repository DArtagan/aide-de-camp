from django.conf.urls import patterns, url, RegexURLResolver
from companies.views import *

from companies import views

def group(regex, *args):
    return RegexURLResolver(regex, args)

urlpatterns = patterns('',
    # Companies
    group(r'^company/',
        url(r'^$', CompanyIndex.as_view(), name='company_index'),
        url(r'^create/$', CompanyCreate.as_view(), name='company_create'),
    ),
    group(r'^positions/',
    ),
)
