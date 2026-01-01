from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.all_posts, name='all_posts'),
    path('weather/', views.weather, name='weather'),
    path('contact/', views.contact, name='contact'),

]