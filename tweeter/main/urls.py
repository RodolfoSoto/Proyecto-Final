from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('main.views',
	url(r'^$', 'home', name='home'),
	url(r'^signup/?$', 'register', name='register'),
	url(r'^tweeting/?$','tweet', name='tweet'),
	url(r'^editProfile/?$','edit', name='edit'),
	url(r'^following/(?P<pk>\d+)?$','follows', name='follows'),
	url(r'^editTweet/(?P<pk>\d+)?$','edit_tweet', name='edit_tweet'),
	url(r'^deleteTweet/(?P<pk>\d+)?$','delete_tweet', name='delete_tweet'),
	url(r'^logout/?$', 'logout_view', name='logout_view'),
	url(r'^reset/?$', 'password_reset', name='password_reset'),
)
