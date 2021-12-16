from django.shortcuts import render
from django.http import JsonResponse, response
from InkItUp.models import *
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


#____________Get tattoos____________

def getAlltattoos(request):
    if request.method == 'GET':
        try:
            tattoos = Tattoo.nodes.all()
            response = []
            for tattoo in tattoos :
                obj = {
                    "description": tattoo.description,
                    "idtattoo":tattoo.idtattoo,
                    "placementonbody": tattoo.placementonbody
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error Occurred"}
            return JsonResponse(response, safe=False)

#____CRUD tattoo____
@csrf_exempt
def tattooDetails(request):
#____Get tattoo by ID____
    if request.method == 'GET':
        idtattoo = request.GET.get('idtattoo', ' ')
        try:
            tattoo = Tattoo.nodes.get(idtattoo=idtattoo)
            response = {
                "description": tattoo.description,
                "idtattoo":tattoo.idtattoo,
                "placementonbody": tattoo.placementonbody
            }
            return JsonResponse(response, safe=False)
        except :
            response = {"error": "Error Occurred"}
            return JsonResponse(response, safe=False)

#____ Create one tattoo ____
    if request.method == 'POST':
        json_data = json.loads(request.body)
        idtattoo = int(json_data['idtattoo'])
        description = json_data['description']
        placementonbody = json_data['placementonbody']
        try:
            tattoo = Tattoo(idtattoo=idtattoo, description=description, placementonbody=placementonbody)
            tattoo.save()
            response = {
                "idtattoo": tattoo.idtattoo,
            }
            return JsonResponse(response)
        except :
            response = {"error": "Error Occurred"}
            return JsonResponse(response, safe=False)
#____Update one tattoo_____
    if request.method == 'PUT':
        json_data = json.loads(request.body)
        idtattoo = int(json_data['idtattoo'])
        description = json_data['description']
        placementonbody = json_data['placementonbody']
        #TVIVL HER
        #uid = json_data['uid']
        try:
            tattoo = Tattoo.nodes.get(idtattoo=idtattoo)
            tattoo.description = description
            tattoo.description = description
            tattoo.save()
            response = {
                "description": tattoo.description,
                "idtattoo":tattoo.idtattoo,
                "placementonbody": tattoo.placementonbody
            }
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

#____Delete tattoo_____
    if request.method == 'DELETE':
        json_data = json.loads(request.body)
        idtattoo = json_data['idtattoo']
        try: 
            tattoo = Tattoo.nodes.get(idtattoo=idtattoo)
            tattoo.delete()
            response = {"success": "tattoo Deleted"}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

