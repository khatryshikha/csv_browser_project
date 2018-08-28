from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name ='home'),
    url(r'^wine/upload', views.check_new_entry, name ='upload'),
    url(r'^wine/result',views.filter_item , name ='result'),
    url(r'^wine/clear', views.clear_database,name ='clear'),
    url(r'^wine/details/(?P<id>\w{0,50})', views.details ,name ='details')
]