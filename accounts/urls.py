from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import profile_views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('auth-receiver', views.auth_receiver, name='auth_receiver'),
    path('profile/', profile_views, name='profile'),    


]
