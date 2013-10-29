from django.conf.urls import patterns, url, include
from companies.views import *

from companies import views

positions = patterns('',
    url(r'^$', PositionIndex.as_view(), name='position_index'),
    url(r'^create/$', PositionCreate.as_view(), name='position_create'),
)

contacts = patterns('',
    url(r'^$', ContactIndex.as_view(), name='contact_index'),
    url(r'^create/$', ContactCreate.as_view(), name='contact_create'),
)

urlpatterns = patterns('',
    # Companies
    url(r'^positions/', include(positions, namespace='position')),
    url(r'^contacts/', include(contacts, namespace='contact')),
    url(r'^$', CompanyIndex.as_view(), name='company_index'),
    url(r'^create/$', CompanyCreate.as_view(), name='company_create'),
)

