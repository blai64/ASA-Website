from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(regex = r'^$',
		view = 'polls.views.pollindex',
		name = 'pollindex'),
    url(regex = r'^(?P<question_id>\d+)/$',
        view = 'polls.views.detail',
        name = 'detail'),
    url(regex = r'^(?P<question_id>\d+)/results/$',
        view = 'polls.views.results',
        name = 'results'),
    url(regex = r'^(?P<question_id>\d+)/vote/$',
        view = 'polls.views.vote',
        name = 'vote'),


    
)


