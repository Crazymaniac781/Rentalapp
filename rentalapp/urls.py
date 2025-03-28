from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_list, name='home_list'),
    path('add/', views.add_rental, name='add_rental'),
    path('rental/<int:pk>/', views.rental_detail, name='rental_detail'),
]
