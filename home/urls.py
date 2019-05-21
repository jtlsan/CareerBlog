from django.urls import path, re_path
from home import views
from django.contrib.auth import views as auth_views
app_name = 'home'
urlpatterns = [
    path('', views.home, name="main"),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('projects/', views.projects, name="projects"),
    path('study/', views.study, name="study"),
    path('study/C/', views.study_c, name="study_c"),
    path('study/django/', views.study_django, name="study_django"),
    path('study/front-end/', views.study_front, name="study_front"),
    path('articles/', views.articles, name="articles"),
    path('articles/it/', views.articles_it, name="articles_it"),
    path('articles/affair/', views.articles_affair, name="articles_affair"),
    path('post_create/', views.post_create, name="post_create"),
    re_path(r'^post/update/(?P<slug_url>[\w-]+)/$', views.post_update, name="post_update"),
    re_path(r'^post/delete/(?P<slug_url>[\w-]+)/$', views.post_delete, name="post_delete"),
    re_path(r'^post/(?P<slug_url>[\w-]+)/$', views.post_detail, name="post_detail"),
]