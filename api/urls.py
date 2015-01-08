from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns(
    'api.views',
    url(r'^account/register', 'register'), )