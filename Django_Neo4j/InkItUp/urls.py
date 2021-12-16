from InkItUp.views.ink import getAllinks
from InkItUp.views.artist import artistDetails
from InkItUp.views.artist import getAllartists
from InkItUp.views.connectors import connectAaTP
from InkItUp.views.Tattooparlor import *
from InkItUp.views.customer import *
from django.conf.urls import url
from InkItUp.views import *
from django.urls import path
urlpatterns =[
    path('customer', customerDetails),
    path('getallcustomers', getAllCustomers),
    path('tattooparlor', tattooparlorDetails),
    path('getalltattooparlors', getAllTattooparlors),
    path('connectaatp', connectAaTP),
    path('getallartists', getAllartists),
    path('artistdetails', artistDetails),
    path('getallinks', getAllinks),

]