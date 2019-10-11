from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^image/(?P<id>[\w-]+)/$',views.display_image,name ='image'),
    url(r'^category/',views.display_category,name ='category'),
    url(r'^location/(?P<location>\D+)/$',views.display_location,name ='location'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)