from django.conf.urls.defaults import patterns, include, url
from RMS import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    ('^$', views.index),
    ('^home/$', views.home),
    ('^dashboard/$', views.dashboard),
    ('^add/$', views.add),
    # Examples:
    # url(r'^$', 'RMS.views.home', name='home'),
    # url(r'^RMS/', include('RMS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
