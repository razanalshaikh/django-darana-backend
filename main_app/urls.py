from django.urls import path
from .views import CitiesListAPI, CityDetailAPI
urlpatterns = [
    path('cities/',CitiesListAPI.as_view(), name='cities_list'),
    path('cities/<int:pk>/',CityDetailAPI.as_view(),name='city_detail')
]