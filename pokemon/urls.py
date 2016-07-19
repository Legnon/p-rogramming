from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.poke_list, name='poke_list'),
    url(r'^json/$', views.poke_json, name='poke_json'),
    url(r'^list/$', views.poke)
]
