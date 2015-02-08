from django.conf.urls import patterns, include, url
from django.contrib import admin
from bets import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^bets/', include('bets.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^create/$', views.CreateRoom.as_view(), name='create'),
    url(r'^room/(?P<url>\w+)/$', views.room_view, name='room'),
    #url(r'^room/(?P<url>\w+)/(?P<venmo_auth>\w+)/$', views.room_view, name='room_venmo'),
    url(r'^make_betroom/$', views.make_betroom, name='make_betroom'),
    url(r'^make_bet/$', views.make_bet, name='make_bet')

)
