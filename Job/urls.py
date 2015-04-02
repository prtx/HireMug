from django.conf.urls import patterns, include, url

urlpatterns = patterns('Job.views',
	url(r'^job_publish/$', 'publish'),
	url(r'^job_detail/(?P<job_id>\d+)/$','detail'),
	url(r'^job_delete/(?P<job_id>\d+)/$','delete'),
	
)
