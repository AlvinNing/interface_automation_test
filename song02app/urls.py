from django.urls import path
from song02app import views

urlpatterns = [
    path('index/', views.home)
]