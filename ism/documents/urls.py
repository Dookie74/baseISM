from django.urls import path
from . import views

urlpatterns = [
    path('', views.documents_main, name='documents_main'),
    path('<str:pk>', views.DocDetailView.as_view(), name='doc_detail')
]
