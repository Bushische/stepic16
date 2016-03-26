from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'qa.views.test'),
    #url(r'^login/$', 'qa.views.test'),
    #url(r'^signup/$', 'qa.views.test'),
    #url(r'^questionOK/(?P<id>\d+)/$', 'qa.views.test'),
    #url(r'^ask/', 'qa.views.test'),
    #url(r'^popularOK/$', 'qa.views.test'),
    #url(r'^new/$', 'qa.views.test'),
    url(r'^question/(?P<inid>\d+)/$', 'qa.views.showquestion', name="question"),
    url(r'^initdb/(?P<cou>\d+)/$', 'qa.views.filldb'),
    url(r'^popular/', 'qa.views.showpopular', name="popular"),
    url(r'^', 'qa.views.showbyid', name="last")
)
