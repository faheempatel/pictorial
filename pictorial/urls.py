from django.conf.urls import patterns, include, url
from django.contrib import admin
from pictorial.views import IndexView, AboutView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pictorial.views.home', name='home'),
    # url(r'^pictorial/', include('pictorial.foo.urls')),
    (r'', IndexView.as_view()),
    (r'^about/', AboutView.as_view()),

    # Django admin site URL's
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
