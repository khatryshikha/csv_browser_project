from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^upload', views.check_new_entry, name ='upload'),
    url(r'^result',views.filter_item , name ='result'),
    url(r'^clear', views.clear_database,name ='clear'),
    url(r'^details/(?P<id>\w{0,50})', views.details ,name ='details')
]