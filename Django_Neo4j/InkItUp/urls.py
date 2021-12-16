from InkItUp.views.ink import getAllinks
from InkItUp.views.artist import artistDetails
from InkItUp.views.artist import getAllartists
from InkItUp.views.connectors import connectAaTP
from InkItUp.views.appointment import *
from InkItUp.views.Tattooparlor import *
from InkItUp.views.customer import *
from django.conf.urls import url
from InkItUp.views import *
from django.urls import path
urlpatterns =[
    path('customer/<str:name>/', customerDetails),
    path('getallcustomers', getAllCustomers),
    path('tattooparlor/<str:name>/', tattooparlorDetails),
    path('getalltattooparlors', getAllTattooparlors),
    path('connectaatp', connectAaTP),
    path('getallartists', getAllartists),
    path('artistdetails/<str:name>/', artistDetails),
    path('getallinks', getAllinks),
    path('getappointment/<int:idappointment>/', appointmentDetails),
    path('getallappointment', getAllappointments),

]