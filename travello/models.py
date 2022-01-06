from django.db import models

# Create your models here.
class Destination(models.Model) :
    # name : str
    # price : int
    # description : str
    # image:str
    # SpecialOffer : bool
    name = models.CharField(max_length=100)
    price =models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to= 'pics')
    SpecialOffer = models.BooleanField(default=False)
        