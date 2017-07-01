from django.conf.urls import url, include
from .views import homeView, ExprienceDetailApi

urlpatterns = [

    url(r'^home/$', homeView, name='home'),
    url(r'^api/$', ExprienceDetailApi.as_view(), name='api'),
]