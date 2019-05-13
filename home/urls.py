from django.urls import path, re_path
from home import views
app_name = 'home'
urlpatterns = [
    path('', views.home, name="main"),
    path('post_create/', views.post_create, name="post_create"),
    re_path(r'^post/update/(?P<slug_url>[\w-]+)/$', views.post_update, name="post_update"),
    re_path(r'^post/(?P<slug_url>[\w-]+)/$', views.post_detail, name="post_detail"),
]