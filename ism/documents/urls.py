from django.urls import path
from . import views

urlpatterns = [
    path('', views.documents_main, name='documents_main'),
]