from logging import fatal
from os import name
from django.shortcuts import render
from django.http import JsonResponse, response
from InkItUp.models import *
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


#____________Get appointments____________

def getAllappointments(request):
    if request.method == 'GET':
        try:
            appointments = Appointment.nodes.all()
            response = []
            for appointment in appointments :
                obj = {
                    "idappointment": appointment.idappointment,
                    "datetime": appointment.datetime,
                    "sessionlenght": appointment.sessionlenght,
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error Occurred"}
            return JsonResponse(response, safe=False)

#____CRUD appointment____
@csrf_exempt
def appointmentDetails(request):
#____Get appointment by Name____
    if request.method == 'GET':
        name = request.GET.get('name', ' ')
        try:
            appointment = Appointment.nodes.get(name=name)
            response = {
                    "idappointment": appointment.idappointment,
                    "datetime": appointment.datetime,
                    "sessionlenght": appointment.sessionlenght,
            }
            return JsonResponse(response, safe=False)
        except :
            response = {"error": "Error Occurred"}
            return JsonResponse(response, safe=False)

#____ Create one appointment ____
    if request.method == 'POST':
        json_data = json.loads(request.body)
        idappointment = json_data ['idappointment']
        datetime = json_data['datetime']
        sessionlenght = int(json_data['sessionlenght'])
        try:
            appointment = Appointment(idappointment=idappointment, datetime=datetime, sessionlenght=sessionlenght)
            appointment.save()
            response = {
                "cpr": appointment.cpr,
            }
            return JsonResponse(response)
        except :
            response = {"error": "Error Occurred"}
            return JsonResponse(response, safe=False)
#____Update one appointment_____
    if request.method == 'PUT':
        json_data = json.loads(request.body)
        idappointment = json_data ['idappointment']
        datetime = json_data['datetime']
        sessionlenght = int(json_data['sessionlenght'])
        
        #TVIVL HER
        #uid = json_data['uid']
        try:
            appointment = Appointment.nodes.get(idappointment=idappointment)
            appointment.datetime
            appointment.sessionlenght
            appointment.save()
            response = {
                "idappointment": appointment.idappointment,
                "datetime": appointment.datetime,
                "sessionlenght": appointment.sessionlenght,
            }
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

#____Delete appointment_____
    if request.method == 'DELETE':
        json_data = json.loads(request.body)
        idappointment = json_data['idappointment']
        try: 
            appointment = Appointment.nodes.get(idappointment=idappointment)
            appointment.delete()
            response = {"success": "appointment Deleted"}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)