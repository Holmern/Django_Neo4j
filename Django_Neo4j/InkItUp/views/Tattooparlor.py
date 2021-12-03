from django.shortcuts import render
from django.http import JsonResponse, response
from Django_Neo4j.InkItUp.models import *
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
'''
    cvr = IntegerProperty(unique_index=True, required=True)
    name = StringProperty(index=True, required=True)
    phonenumber = IntegerProperty(index=True, required=True)
    adress = StringProperty(index=True, required=True)
    email = StringProperty(index=True, required=True)
'''


#____________Get tattooparlors____________

def getAlltattooparlors(request):
    if request.method == 'GET':
        try:
            tattooparlors = Tattooparlor.nodes.all()
            response = []
            for tattooparlor in tattooparlors :
                obj = {
                    "cvr": tattooparlor.cvr,
                    "name": tattooparlor.name,
                    "phonenumber": tattooparlor.phonenumber,
                    "adress": tattooparlor.adress,
                    "email": tattooparlor.email,
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error Occurred"}
            return JsonResponse(response, safe=False)

#____CRUD tattooparlor____
@csrf_exempt
def tattooparlorDetails(request):
#____Get tattooparlor by Name____
    if request.method == 'GET':
        name = request.GET.get('name', ' ')
        try:
            tattooparlor = Tattooparlor.nodes.get(name=name)
            response = {
                "cvr": tattooparlor.cvr,
                "name": tattooparlor.name,
                "phonenumber": tattooparlor.phonenumber,
                "adress": tattooparlor.adress,
                "email": tattooparlor.email
            }
            return JsonResponse(response, safe=False)
        except :
            response = {"error": "Error Occurred"}
            return JsonResponse(response, safe=False)

#____ Create one tattooparlor ____
    if request.method == 'POST':
        json_data = json.loads(request.body)
        cvr = int(json_data['cvr'])
        name = json_data['name']
        phonenumber = int(json_data['phonenumber'])
        adress = json_data['adress']
        email = json_data['email']
        try:
            tattooparlor = Tattooparlor(cvr=cvr, name=name, phonenumber=phonenumber, adress=adress, email=email)
            tattooparlor.save()
            response = {
                "cvr": tattooparlor.cvr,
            }
            return JsonResponse(response)
        except :
            response = {"error": "Error Occurred"}
            return JsonResponse(response, safe=False)
#____Update one tattooparlor_____
    if request.method == 'PUT':
        json_data = json.loads(request.body)
        cvr = int(json_data['cvr'])
        name = json_data['name']
        phonenumber = int(json_data['phonenumber'])
        adress = json_data['adress']
        email = json_data['email']
        #TVIVL HER
        #uid = json_data['uid']
        try:
            tattooparlor = Tattooparlor.nodes.get(cvr=cvr)
            tattooparlor.name = name
            tattooparlor.email = email
            tattooparlor.save()
            response = {
                "cvr": tattooparlor.cvr,
                "name": tattooparlor.name,
                "phonenumber": tattooparlor.phonenumber,
                "adress": tattooparlor.adress,
                "email": tattooparlor.email,
            }
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

#____Delete tattooparlor_____
    if request.method == 'DELETE':
        json_data = json.loads(request.body)
        cvr = json_data['cvr']
        try: 
            tattooparlor = Tattooparlor.nodes.get(cvr=cvr)
            tattooparlor.delete()
            response = {"success": "tattooparlor Deleted"}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)