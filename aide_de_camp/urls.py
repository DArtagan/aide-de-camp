from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aide_de_camp.views.home', name='home'),
    # url(r'^aide_de_camp/', include('aide_de_camp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^accounts/login/', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^companies/', include('companies.urls', namespace="company")),
    #url(r'^', include('companies.urls', namespace="company")),
)
