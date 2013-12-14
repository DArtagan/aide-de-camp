from django.conf.urls import patterns, url, include
from companies.views import *

urlpatterns = patterns('',
    url(r'^$', QuestionIndex.as_view(), name='question_index'),
    url(r'^create/$', QuestionCreate.as_view(), name='question_create'),
    url(r'^(?P<pk>\d+)/$', QuestionDetail.as_view(), name='question_detail'),
    url(r'^(?P<pk>\d+)/update/$', QuestionUpdate.as_view(), name='question_update'),
    url(r'^(?P<pk>\d+)/delete/$', QuestionDelete.as_view(), name='question_delete'),
)

