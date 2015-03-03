from django.conf.urls import patterns, url

from polls import views

urlpatterns = pattern ('',
	url(r'^$', views.index, name='index'),
)
