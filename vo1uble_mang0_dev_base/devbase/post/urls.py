from django.urls import path
from .views import *

urlpatterns = [
    path('add_post/', AddPostClass.as_view(), name='add_post'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', Home.as_view(), name='home'),
    path('mainpage/', Home.as_view(), name='mainpage'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('search/', Search.as_view(), name='search'),
]
from .views import *

