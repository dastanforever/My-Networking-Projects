

from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns=[
	
	url(r'^$', TemplateView.as_view( template_name='echo_server/index.html' ), name='index' ),

	]