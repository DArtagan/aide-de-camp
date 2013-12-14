from django.conf.urls import patterns, url, include
from questions.views import *

urlpatterns = patterns('',
    url(r'^$', QuestionIndex.as_view(), name='index'),
    url(r'^create/$', QuestionCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', QuestionDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', QuestionUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', QuestionDelete.as_view(), name='delete'),
)

