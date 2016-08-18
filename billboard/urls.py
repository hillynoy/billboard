
from django.conf.urls import include, url
from django.contrib import admin
from post import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^post', include('post.urls')),
    url(r'^post/create_message$', views.create_message, name='create'),
]
