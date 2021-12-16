from InkItUp.models import *
from django.shortcuts import render
from django.http import JsonResponse, response
from InkItUp.models import *
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
'''
  batchnumber = IntegerProperty(unique_index=True, required=True)
    brand = StringProperty(index=True, required=True)
    colorcode = StringProperty(index=True, required=True)
    experationdate = StringProperty(required=True)
    price = FloatProperty(index=True, required=True)
'''

#____________Get inks____________

def getAllinks(request):
    if request.method == 'GET':
        try:
            inks = Ink.nodes.all()
            response = []
            for ink in inks :
                obj = {
                    "batchnumber": ink.batchnumber,
                    "brand":ink.brand,
                    "colorcode": ink.colorcode,
                    "experationdate":ink.experationdate,
                    "price": ink.price
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error Occurred"}
            return JsonResponse(response, safe=False)

#____CRUD ink____
@csrf_exempt
def inkDetails(request):
#____Get ink by ID____
    if request.method == 'GET':
        batchnumber = request.GET.get('batchnumber', ' ')
        try:
            ink = Ink.nodes.get(batchnumber=batchnumber)
            response = {
                "batchnumber": ink.batchnumber,
                "brand":ink.brand,
                "colorcode": ink.colorcode,
                "experationdate":ink.experationdate,
                "price": ink.price
            }
            return JsonResponse(response, safe=False)
        except :
            response = {"error": "Error Occurred"}
            return JsonResponse(response, safe=False)

'''#___Get Customer By Ink____
    if request.method =='GET':
        batchnumber.request.GET.get('batchnumber', ' ')
        try:
            ink = Ink.nodes.get(batchnumber=batchnumber)
            customer = Customer.nodes.get(name=name)'''
            
