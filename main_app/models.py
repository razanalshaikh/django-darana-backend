from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
        
FEATURES = (
    ('AD','Adventure'),
    ('NT', 'Nature'),
    ('CH','Culture & History'),
    ('SH','Shopping'),
    ('BR','Beauty & Relax'),
    ('SP','Sports'),
    ('ET','Entertainment'),
    ('LS','Luxury')
    )
    
class Feature(models.Model):
    name = models.CharField(
        max_length= 2,
        choices= FEATURES,
        default=FEATURES[0][0]
    )
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
