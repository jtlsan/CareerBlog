from django.urls import path
from home import views
app_name = 'home'
urlpatterns = [
    path('', views.home, name="main"),
    path('post_create/', views.post_create, name="post_create"),
]