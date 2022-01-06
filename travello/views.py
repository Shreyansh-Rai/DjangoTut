from django.db.models.fields import PositiveBigIntegerField
from django.http import request
from django.shortcuts import render
from .models import Destination
# Create your views here.

def index (request):

    # dest1 = Destination()
    # dest1.name = "Mumbai"
    # dest1.price = 700
    # dest1.description = "The city that never sleeps"
    # dest1.image = "destination_1.jpg"
    # dest1.SpecialOffer = False
    # dest3 = Destination()
    # dest3.name = "Tokyo"
    # dest3.price = 900
    # dest3.description = "Ching cheng ha- oh wait, sorry, I meant anime was daisuki"
    # dest3.image = "destination_3.jpg"
    # dest3.SpecialOffer = True
    # dest2 = Destination()
    # dest2.name = "Paris"
    # dest2.price = 1000
    # dest2.description = "Fancy city with big metal tower"
    # dest2.image = "destination_2.jpg"
    # dest2.SpecialOffer = False
    dests = Destination.objects.all()
    context = {
        "dests" : dests
    }
    return render(request,"index.html",context)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!HOW TO MIGRATE DB!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Toh dekha bhai pahli baat toh ye hai ki in models you gotta make your class cool? mow once you are done with that you can 
# extend Model and assing fields to the variables and then what you can do is make sure ki A) your app is added to the setting.py
# by simply adding the name there and then what you need ot make sure you are doing is that your database that you made in Postgres
# should be properly entered via pgadmin now when the time comes to connect them what you need to do is visit the databases section
# of the settings.py and then you can legit go ahead and python manage,py makemigrations that stuff and then to finally make that
# stuff go to the database you go python manage.py sqlmigrate appname 0001 then give migrate cmd