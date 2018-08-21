from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^wine/upload', views.check_new_entry)
]