from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'HireMug.views.home', name='home'),
    
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    
    (r'^', include('Company.urls')),
    (r'^', include('Job.urls')),
)
