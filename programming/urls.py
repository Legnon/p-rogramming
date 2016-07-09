from django.conf.urls import url, include
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.introduce),
    url(r'^', include('blog.urls', namespace='blog')),
]
