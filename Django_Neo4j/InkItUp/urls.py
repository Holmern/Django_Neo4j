from InkItUp.views.connectors import connectAaTP
from InkItUp.views.Tattooparlor import *
from InkItUp.views.customer import *
from django.conf.urls import url
from InkItUp.views import *
from django.urls import path
urlpatterns =[
    path('customer', customerDetails),
    path('getAllCustomers', getAllCustomers),
    path('tattooparlor', tattooparlorDetails),
    path('getAllTattooparlors', getAllTattooparlors),
    path('connectAaTP', connectAaTP)
]