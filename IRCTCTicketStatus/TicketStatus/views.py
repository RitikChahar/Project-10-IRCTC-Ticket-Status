from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from TicketStatus.functions.ticket_status import checkTicketStatus 
from TicketStatus.functions.email_sender import send_email 
import json

@csrf_exempt
def ticket_status(request):
    try:
        pnr_number = str(request.GET.get('pnr_number'))
        data = checkTicketStatus(pnr_number)
        return JsonResponse({
            "success":True,
            "message": "All good, here if your data!",
            "data":data
        })
    except:
        return JsonResponse({
            "success":False,
            "message": "Something went wrong, stay connected!"
        })
    
@csrf_exempt
def send_status(request):
    if (request.method=="POST"):
        request_data=json.loads(request.body)
        try:
            send_email(request_data)
            return JsonResponse({
                "success":True,
                "message": "All good, your mail is sent!",
            })
        except:
            return JsonResponse({
                "success":False,
                "message": "Something went wrong, stay connected!"
            })
    else:
        return HttpResponse("Method Not Allowed")   