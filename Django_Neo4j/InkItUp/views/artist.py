from logging import fatal
from os import name
from django.shortcuts import render
from django.http import JsonResponse, response
from InkItUp.models import *
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


#____________Get artists____________

def getAllartists(request):
    if request.method == 'GET':
        try:
            artists = Artist.nodes.all()
            response = []
            for artist in artists :
                obj = {
                    "cpr": artist.cpr,
                    "name": artist.name,
                    "email": artist.email,
                    "phonenumber": artist.phonenumber
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error Occurred"}
            return JsonResponse(response, safe=False)

#____CRUD artist____
@csrf_exempt
def artistDetails(request, name):
#____Get artist by Name____
    if request.method == 'GET':
        #name = request.GET.get('name', ' ')
        try:
            artist = Artist.nodes.get(name=name)
            response = {
                "cpr": artist.cpr,
                "name": artist.name,
                "email": artist.email,
                "phonenumber": artist.phonenumber
            }
            return JsonResponse(response, safe=False)
        except :
            response = {"error": "Error Occurred"}
            return JsonResponse(response, safe=False)

#____ Create one artist ____
    if request.method == 'POST':
        json_data = json.loads(request.body)
        cpr = int(json_data['cpr'])
        name = json_data['name']
        email = json_data['email']
        phonenumber = int(json_data['phonenumber'])
        try:
            artist = Artist(cpr=cpr, name=name, email=email, phonenumber=phonenumber)
            artist.save()
            response = {
                "cpr": artist.cpr,
            }
            return JsonResponse(response)
        except :
            response = {"error": "Error Occurred"}
            return JsonResponse(response, safe=False)
#____Update one artist_____
    if request.method == 'PUT':
        json_data = json.loads(request.body)
        cpr = int(json_data['cpr'])
        name = json_data['name']
        email = json_data['email']
        phonenumber = int(json_data['phonenumber'])
        #TVIVL HER
        #uid = json_data['uid']
        try:
            artist = Artist.nodes.get(cpr=cpr)
            artist.name = name
            artist.email = email
            artist.phonenumber = phonenumber
            artist.save()
            response = {
                "cpr": artist.cpr,
                "name": artist.name,
                "email": artist.email,
                "phonenumber": artist.phonenumber
            }
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

#____Delete artist_____
    if request.method == 'DELETE':
        json_data = json.loads(request.body)
        cpr = json_data['cpr']
        try: 
            artist = Artist.nodes.get(cpr=cpr)
            artist.delete()
            response = {"success": "artist Deleted"}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)