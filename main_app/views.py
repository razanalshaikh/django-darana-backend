from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from main_app.models import City
from .serializers import CitySerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.


class CitiesListAPI(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        cities = City.objects.all()
        serializer = CitySerializer(cities,many=True)
        return Response(serializer.data,status=200)
    