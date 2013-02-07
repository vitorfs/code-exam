from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'exams.views.user_exams'),
    (r'^login/$', 'home.views.login'),
    (r'^logout/$', 'home.views.logout'),
    url(r'^prova/', include('exams.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()