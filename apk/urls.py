from django.urls import path
from .views import *
urlpatterns = [
    path('',user_register,name="user_register_link"),
    path('login_page',user_login,name="user_login_link"),
    path('user_logout',user_logout,name="user_logout_link"),
    path('home_page',user_home,name="user_home_link")
]

