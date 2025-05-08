from django.db import models
# from django.contrib.gis.db import models
# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    def __str__(self):
        return self.name
        
FEATURES = (
    ('Adventure','Adventure'),
    ('Nature', 'Nature'),
    ('Culture & History','Culture & History'),
    ('Shopping','Shopping'),
    ('Beauty & Relax','Beauty & Relax'),
    ('Sports','Sports'),
    ('Entertainment','Entertainment'),
    ('Luxury','Luxury')
    )
    
class Feature(models.Model):
    name = models.CharField(
        max_length= 30,
        choices= FEATURES,
        default=FEATURES[0][0]
    )
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

        
CATEGORIES = (
    ('Nature', 'Nature'),
    ('Culture & History','Culture & History'),
    ('Shopping','Shopping'),
    ('Entertainment','Entertainment'),
    ('Food & Beverages','Food & Beverages'),
    ('Adventure','Adventure'),
)

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.CharField(max_length=255)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    category = models.CharField(
        max_length = 20,
        choices=CATEGORIES,
        default= CATEGORIES[0][0]
    )

    def __str__(self):
        return self.name

    