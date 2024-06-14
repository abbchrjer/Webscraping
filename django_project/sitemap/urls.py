from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('maps/', views.maps, name='maps'),
    path('path/', views.path, name='path'),
]