from django.conf.urls import url
from . import views #The period here means we're importing from the current package, This is a relative import.

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
