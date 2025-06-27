from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import profile_views
from .views import profile_update

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('auth-receiver', views.auth_receiver, name='auth_receiver'),
    path('upload-avatar/', views.upload_avatar, name='upload_avatar'),
    path('profile/', profile_views, name='profile'),    
    path('profile/update/', profile_update, name='profile_update'),

]
