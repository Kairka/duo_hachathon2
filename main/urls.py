from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('region/<str:slug>/', region_detail, name='region'),
    path('tour-detail/<int:pk>/', detail, name='detail'),
    path('add-tour/', add_tour, name='add'),
    path('update-tour/<int:pk>/', update_tour, name='update'),
    path('delete-tour/<int:pk>/', DeleteTourView.as_view(), name='delete'),
]