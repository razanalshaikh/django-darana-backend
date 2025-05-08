from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main_app.models import CATEGORIES, City, Feature, Place, FEATURES
from .serializers import CitySerializer,FeatureSerializer, PlaceSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class CitiesListAPI(APIView):
    permission_classes = [AllowAny]
    # get city
    def get(self,request):
        cities = City.objects.all()
        serializer = CitySerializer(cities,many=True)
        return Response(serializer.data,status=200)
    # post city
    def post(self,request):
        if request.user.is_staff:
            serializer = CitySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
class CityDetailAPI(APIView):
    permission_classes = [AllowAny]

    def get_object(self,pk):
        return get_object_or_404(City,pk=pk)
    
    def get(self,request,pk):
        city = self.get_object(pk)
        serializer = CitySerializer(city)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self,request,pk):
        if request.user.is_staff or  request.user.is_superuser:
            city = self.get_object(pk)
            city.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    def patch(self,request,pk):
        if request.user.is_staff:
            city = self.get_object(pk)
            serializer = CitySerializer(city,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    
class FeatureListAPI(APIView):
    permission_classes = [AllowAny]
    
    def get(self,request,pk):
        features = Feature.objects.all().filter(city_id = pk)
        serializer = FeatureSerializer(features, many = True)
        return Response(serializer.data,status=200)
    
    def post(self,request,pk):
        
        if request.user.is_staff:
                city = get_object_or_404(City,pk = pk)
                data = request.data.copy() # make a copy
                data['city'] = city.pk
                serializer = FeatureSerializer(data=data)
                if serializer.is_valid(): 
                    serializer.save()
                    return Response(serializer.data,status=201)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class PlaceListAPI(APIView):
    permission_classes = [AllowAny]
    
    def get(self,request):
        places = Place.objects.all()
        serializer = PlaceSerializer(places,many=True)
        return Response(serializer.data,status=200)
    
    def post(self,request):
        if request.user.is_staff:
            serializer = PlaceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    

class PlaceListByCityAPI(APIView):
    permission_classes = [AllowAny]

    def get(self,request, city_id):
        places = Place.objects.all().filter(city_id=city_id)
        serializer = PlaceSerializer(places, many = True)
        return Response(serializer.data,status=200)
    
    def get_object(self,pk):
        return get_object_or_404(City,pk=pk)
    
class PlaceDetailAPI(APIView):
    permission_classes = [AllowAny]

    def get_object(self,pk):
        return get_object_or_404(Place,pk=pk)

    def get(self,request,pk):
        place = self.get_object(pk=pk)
        serializer = PlaceSerializer(place)
        return Response(serializer.data,status=status.HTTP_200_OK)        
    
    def patch(self,request,pk):
        if request.user.is_staff:
            place = get_object_or_404(Place, pk=pk)
            serializer = PlaceSerializer(place,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self,request,pk):
        if request.user.is_staff or  request.user.is_superuser:
            place = get_object_or_404(Place,pk=pk)
            place.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

# I found this suggested solution to get categories option to frontend 
# https://stackoverflow.com/questions/74944828/django-rest-framework-get-all-options-for-choice-field
class CatergoryChoicesList(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        # I will do using list-comprehensions
        choices = [category[0] for category in CATEGORIES ]
        return Response(choices, status=status.HTTP_200_OK)
    
# Add signup
class SignUpView(APIView):
    permission_classes = [AllowAny]
    # When we recieve a POST request with username, email, and password. Create a new user.
    def post(self, request):
        # Using .get will not error if there's no username
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            validate_password(password)
        except ValidationError as err:
            return Response({'error': err.messages}, status=400)

        # Actually create the user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # create an access and refresh token for the user and send this in a response
        tokens = RefreshToken.for_user(user)
        return Response(
            {
                'refresh': str(tokens),
                'access': str(tokens.access_token)
            },
            status=201
        )