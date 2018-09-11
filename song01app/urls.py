from django.urls import path
from song01app import views

urlpatterns = [
    path('upload/', views.upload_file)
]