from django.urls import path
from .views import (
    CitiesListAPI, 
    CityDetailAPI, 
    FeatureListAPI, 
    PlaceListAPI, 
    PlaceListByCityAPI,
    PlaceDetailAPI,
    CatergoryChoicesList
)
urlpatterns = [
    path('cities/',CitiesListAPI.as_view(), name='cities_list'),
    path('cities/<int:pk>/',CityDetailAPI.as_view(),name='city_detail'),

    path('cities/<int:pk>/features/',FeatureListAPI.as_view(), name='city_features' ),
    path('places/',PlaceListAPI.as_view(), name='places_list'),
    path('cities/<int:city_id>/places',PlaceListByCityAPI.as_view(), name='places_list_by_City'),
    path('places/<int:pk>/',PlaceDetailAPI.as_view(), name='place_details'),
    path('categories/',CatergoryChoicesList.as_view(), name='category_choices')

]