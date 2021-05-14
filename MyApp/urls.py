from django.urls import path
from .views.Index import Index
from .views.Login import Login , logout
from .views.Signup import Signup
from .views.Home import Home


urlpatterns = [
    path('',Index.as_view(),name='home' ),
    path('signup',Signup.as_view(),name='signup'),
    path('login',Login.as_view(),name='login'),
    path('home',Home.as_view(),name='homeIndex'),
    path('logout',logout,name='logout')

]