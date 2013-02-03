from django.conf.urls import patterns, include, url
from django.contrib import admin
from home.views import homepage, login, logout, prova
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', homepage),
    (r'^login/', login),
    (r'^logout/', logout),
    url(r'^prova/(?P<exam_id>\d+)/$', prova),
    #url(r'^prova/(?P<exam_id>\d+)/questao/(?P<question_id>\d+)/$', 'prova'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()