from django.http import JsonResponse, response
from Django_Neo4j.InkItUp.models import *
from django.views.decorators.csrf import csrf_exempt
import json
#Herinde har vi vores connections mellem enheder - Eksempel connect AaTP = Artist And TattooParlor

#Cross Site Request Forgery -- Er middleware som beskytter mod at andre hjemmesider kan benytte sig af brugerens cookies
# - fx login oplysninger, som så kan gøre slemme ting ved din hjemmeside
@csrf_exempt
def connectAaTP(request):
    if request.method == 'PUT':
        json_data = json.loads(request.body)
        cpr = json_data['cpr']
        cvr = json_data['cvr']
        try:
            Customer.nodes.get(cpr=cpr)
            Tattooparlor.nodes.get(cvr=cvr)
            res = Customer.Tatooparlor.connect(Tattooparlor)
            response = {"result": res}
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error Occurred"}
