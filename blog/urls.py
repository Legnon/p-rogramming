from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^add_post/', views.post_add, name='post_add'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
