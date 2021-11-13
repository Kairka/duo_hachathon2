from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('region/<str:slug>/', region_detail, name='region'),
    path('tour-detail/<int:pk>/', detail, name='detail'),
    path('add-tour/', add_tour, name='add'),
    path('update-tour/<int:pk>/', update_tour, name='update'),
    path('delete-tour/<int:pk>/', delete_tour, name='delete'),
]