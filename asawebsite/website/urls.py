from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'asawebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(regex = r'^$',
    	view = 'website.views.home',
    	name = 'home'),

    url(regex = r'^about/$',
    	view = 'website.views.about',
    	name = 'about'),

    url(regex = r'^events/$',
    	view = 'website.views.events',
    	name = 'events'),

    url(regex = r'^gallery/$',
    	view = 'website.views.gallery',
    	name = 'gallery'),

    url(regex = r'^board/$',
    	view = 'website.views.board',
    	name = 'board'),

    

    url(r'^admin/', include(admin.site.urls)),
)
