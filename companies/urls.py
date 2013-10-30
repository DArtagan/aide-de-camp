from django.conf.urls import patterns, url, include
from companies.views import *

from companies import views

positions = patterns('',
    url(r'^$', PositionIndex.as_view(), name='position_index'),
    url(r'^create/$', PositionCreate.as_view(), name='position_create'),
    url(r'^(?P<pk>\d+)/$', PositionDetail.as_view(), name='position_detail'),
    url(r'^(?P<pk>\d+)/update/$', PositionUpdate.as_view(), name='position_update'),
    url(r'^(?P<pk>\d+)/delete/$', PositionDelete.as_view(), name='position_delete'),
)

contacts = patterns('',
    url(r'^$', ContactIndex.as_view(), name='contact_index'),
    url(r'^create/$', ContactCreate.as_view(), name='contact_create'),
    url(r'^(?P<pk>\d+)/$', ContactDetail.as_view(), name='contact_detail'),
    url(r'^(?P<pk>\d+)/update/$', ContactUpdate.as_view(), name='contact_update'),
    url(r'^(?P<pk>\d+)/delete/$', ContactDelete.as_view(), name='contact_delete'),
)

urlpatterns = patterns('',
    # Companies
    url(r'^positions/', include(positions, namespace='position')),
    url(r'^contacts/', include(contacts, namespace='contact')),
    url(r'^$', CompanyIndex.as_view(), name='company_index'),
    url(r'^create/$', CompanyCreate.as_view(), name='company_create'),
    url(r'^(?P<pk>\d+)/$', CompanyDetail.as_view(), name='company_detail'),
    url(r'^(?P<pk>\d+)/update/$', CompanyUpdate.as_view(), name='company_update'),
    url(r'^(?P<pk>\d+)/delete/$', CompanyDelete.as_view(), name='company_delete'),
)

