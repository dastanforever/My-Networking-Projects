
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.contrib import admin


from socketio import sdjango
sdjango.autodiscover()


urlpatterns = [
    # Examples:
    # url(r'^$', 'socketioapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('echo_server.urls')),
    url(r'^socket\.io', include(sdjango.urls)),
]
