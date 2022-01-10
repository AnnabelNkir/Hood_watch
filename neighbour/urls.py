from django.urls import include, path
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
   path(r'^$',views.index,name='index'),
   path(r'^signup/$', views.signup, name='signup'),
   path(r'^profile/',views.profile,name = 'profile'),
   path(r'^profiles/(\d+)',views.profiles,name='profiles'),
   path(r'^create/', views.create, name='create'),
   path(r'^biz/', views.biz, name='biz'),
   path(r'^hood/(\d+)', views.hood, name='hood'),
   path(r'^search/', views.search_results, name='search_results'),
   path(r'^post/', views.post, name='post'),
   path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)