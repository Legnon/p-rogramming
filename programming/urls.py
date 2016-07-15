from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.introduce),
    url(r'^pokemon/', include('pokemon.urls', namespace='pokemon')),
    url(r'^', include('blog.urls', namespace='blog')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
