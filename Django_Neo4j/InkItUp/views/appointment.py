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
                    "date": appointment.date,
                    "time": appointment.time,
                    "sessionlenght": appointment.sessionlenght,
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error Occurred"}
            return JsonResponse(response, safe=False)

#____CRUD appointment____
@csrf_exempt
def appointmentDetails(request, appointmentid):
#____Get appointment by ID____
    if request.method == 'GET':
        #name = request.GET.get('name', ' ')
        try:
            appointment = Appointment.nodes.get(appointmentid=appointmentid)
            response = {
                    "idappointment": appointment.idappointment,
                    "date": appointment.date,
                    "time": appointment.time,
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
        date = json_data['date']
        time = json_data['time']
        sessionlenght = int(json_data['sessionlenght'])
        try:
            appointment = Appointment(idappointment=idappointment, date=date, time=time, sessionlenght=sessionlenght)
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
        date = json_data['date']
        time = json_data['time']
        sessionlenght = int(json_data['sessionlenght'])
        
        #TVIVL HER
        #uid = json_data['uid']
        try:
            appointment = Appointment.nodes.get(idappointment=idappointment)
            appointment.date
            appointment.time
            appointment.sessionlenght
            appointment.save()
            response = {
                "idappointment": appointment.idappointment,
                "date": appointment.date,
                "time": appointment.time,
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