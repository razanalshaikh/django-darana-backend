from django.urls import path
from .views import CitiesListAPI
urlpatterns = [
    path('cities/',CitiesListAPI.as_view(), name='cities-list')
]