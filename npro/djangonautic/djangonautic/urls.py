from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
#this is for static files for styling like stuff
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#this is for uploading images
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^about/$', views.about),
    url(r'^$', views.home),
#    path('^admin/', admin.site.urls),
 #   path('^about/$', views.about),
  #  path('^$', views.home),

]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)