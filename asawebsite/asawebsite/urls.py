from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'asawebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('website.urls')),
    url(r'^polls/', include('polls.urls', namespace = "polls")),


    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG :
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
