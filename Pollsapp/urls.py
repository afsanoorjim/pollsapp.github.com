from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('addopt', views.addopt, name='addopt'),
    path('vote/<int:pk>/', views.vote, name='vote'),
    path('result/<int:pk>/', views.result, name='result'),
]