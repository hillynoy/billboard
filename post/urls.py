from django.conf.urls import url
from . import views

app_name = 'post'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^create_message$', views.create_message, name='create'),
    url(r'^register$', views.register, name='register'),
]