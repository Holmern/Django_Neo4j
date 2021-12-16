from django.shortcuts import render
from django.http import JsonResponse, response
from InkItUp.models import *
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


#____________Get Customers____________

def getAllCustomers(request):
    if request.method == 'GET':
        try:
            customers = Customer.nodes.all()
            response = []
            for customer in customers :
                obj = {
                    "cpr": customer.cpr,
                    "name": customer.name,
                    "email": customer.email
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error Occurred"}
            return JsonResponse(response, safe=False)

#____CRUD CUSTOMER____
@csrf_exempt
def customerDetails(request):
#____Get Customer by Name____
    if request.method == 'GET':
        name = request.GET.get('name', ' ')
        try:
            customer = Customer.nodes.get(name=name)
            response = {
                "cpr": customer.cpr,
                "name": customer.name,
                "email": customer.email
            }
            return JsonResponse(response, safe=False)
        except :
            response = {"error": "Error Occurred"}
            return JsonResponse(response, safe=False)

#____ Create one Customer ____
    if request.method == 'POST':
        json_data = json.loads(request.body)
        cpr = int(json_data['cpr'])
        name = json_data['name']
        email = json_data['email']
        try:
            customer = Customer(cpr=cpr, name=name, email=email)
            customer.save()
            response = {
                "cpr": customer.cpr,
            }
            return JsonResponse(response)
        except :
            response = {"error": "Error Occurred"}
            return JsonResponse(response, safe=False)
#____Update one Customer_____
    if request.method == 'PUT':
        json_data = json.loads(request.body)
        cpr = int(json_data['cpr'])
        name = json_data['name']
        email = json_data['email']
        #TVIVL HER
        #uid = json_data['uid']
        try:
            customer = Customer.nodes.get(cpr=cpr)
            customer.name = name
            customer.email = email
            customer.save()
            response = {
                "cpr": customer.cpr,
                "name": customer.name,
                "email": customer.email,
            }
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

#____Delete Customer_____
    if request.method == 'DELETE':
        json_data = json.loads(request.body)
        cpr = json_data['cpr']
        try: 
            customer = Customer.nodes.get(cpr=cpr)
            customer.delete()
            response = {"success": "Customer Deleted"}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

