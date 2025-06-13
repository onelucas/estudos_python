from django.urls import path
from .views import index, livro

urlpatterns = [
    path('', index),
    path('Livro/<int:pk>', livro, name = 'Livro')
]