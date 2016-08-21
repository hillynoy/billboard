
from django.conf.urls import include, url
from django.contrib import admin
from post import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^post/', include('post.urls',  namespace ='post')),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logged_out/$', logout, {'next_page': '/post'}),
]
