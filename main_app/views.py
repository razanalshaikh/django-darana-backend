from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main_app.models import City, Feature, Place
from .serializers import CitySerializer,FeatureSerializer, PlaceSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404


class CitiesListAPI(APIView):
    permission_classes = [AllowAny]
    # get city
    def get(self,request):
        cities = City.objects.all()
        serializer = CitySerializer(cities,many=True)
        return Response(serializer.data,status=200)
    # post city
    def post(self,request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CityDetailAPI(APIView):
    permission_classes = [AllowAny]

    def get_object(self,pk):
        return get_object_or_404(City,pk=pk)
    
    def get(self,request,pk):
        city = self.get_object(pk)
        serializer = CitySerializer(city)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self,request,pk):
        city = self.get_object(pk)
        city.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def patch(self,request,pk):
        city = self.get_object(pk)
        serializer = CitySerializer(city,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class FeatureListAPI(APIView):
    permission_classes = [AllowAny]
    
    def get(self,request,pk):
        features = Feature.objects.all().filter(city_id = pk)
        serializer = FeatureSerializer(features, many = True)
        return Response(serializer.data,status=200)
    
    def post(self,request,pk):
        city = get_object_or_404(City,pk = pk)
        data = request.data.copy() # make a copy
        data['city'] = city.pk

        serializer = FeatureSerializer(data=data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PlaceListAPI(APIView):
    permission_classes = [AllowAny]
    
    def get(self,request):
        places = Place.objects.all()
        serializer = PlaceSerializer(places,many=True)
        return Response(serializer.data,status=200)
    
    def post(self,request):
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        # if anything happens, erorr then 400 bad request
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


