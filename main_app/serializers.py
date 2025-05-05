from rest_framework import serializers
from .models import FEATURES, City, Feature, Place

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

# this link helped me to return the human readable value instead of the actual value
#  (example: Actual Value: NT, Human readable Value: Nature)
# https://stackoverflow.com/questions/49256851/how-to-serialize-tuples-in-django-rest-framework-or-is-there-any-way-to-conver

class FeatureSerializer(serializers.ModelSerializer):
    name = serializers.ChoiceField(choices=FEATURES)

    class Meta:
        model = Feature
        fields = '__all__'
    
    def get_name(self, obj):
        return obj.get_name_display()

    
class PlaceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Place
        fields = '__all__'

