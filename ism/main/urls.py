from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('contact', views.contact, name='contacts')

]