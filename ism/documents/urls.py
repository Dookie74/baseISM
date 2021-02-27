from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf.urls.static import serve

urlpatterns = [
    path('', views.documents_main, name='documents_main'),
    path('<str:pk>', views.DocDetailView.as_view(), name='doc_detail'),
]

