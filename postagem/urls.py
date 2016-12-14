from django.conf.urls import url
from .views import teste

urlpatterns = [
	url(r'^$', teste, name='teste')
]