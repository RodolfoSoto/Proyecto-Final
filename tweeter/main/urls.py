from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('main.views',
	url(r'^$', 'home', name='home'),
	url(r'^signup/?$', 'register', name='register'),
	url(r'^tweeting/?$','tweet', name='tweet'),
	url(r'^editProfile/?$','edit', name='edit'),

)
