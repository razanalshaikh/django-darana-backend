from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main_app.models import City
from .serializers import CitySerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404


class CitiesListAPI(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        cities = City.objects.all()
        serializer = CitySerializer(cities,many=True)
        return Response(serializer.data,status=200)

class CityDetailAPI(APIView):
    permission_classes = [AllowAny]

    def get_object(self,pk):
        return get_object_or_404(City,pk=pk)
    
    def get(self,request,pk):
        city = self.get_object(pk)
        serializer = CitySerializer(city)
        return Response(serializer.data,status=status.HTTP_200_OK)
