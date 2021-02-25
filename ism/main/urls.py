from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main'),
    path('contact', views.contact, name='contacts'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout')

]

