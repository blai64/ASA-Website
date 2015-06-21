from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'asawebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('website.urls')),
    url(r'^polls/', include('polls.urls', namespace = "polls")),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),


    url(r'^admin/', include(admin.site.urls)),
)
