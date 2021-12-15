from django.shortcuts import render
from django.http import JsonResponse
import json
from datetime import datetime
from .models import Event


def version_endpoint(request):
    return JsonResponse({
        "version": 10.150,
    })


def hello_endpoint(request):
    if request.method == "POST":
        data = json.loads(request.body)



        name = data.get("name")



        return JsonResponse({
            "msg": "Welcome " + name,
        })
    else:
        return JsonResponse({
            "msg": "crappy method",
        }, status=405)

def list_create_event_api_endpoint(request):
    if request.method == "GET":
        results = [
            {
                "id": 1,
                "event_name": "Party",
                "event_address": "123Boulevar North",
                "event_p_c": "N6G 0C4",
                "event_dt": "",
                "filters": "",
                "event_details" : "Details from the user",

            }
        ]
        return JsonResponse({"results": results})
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"msg":"Fill the forms"}, status=400 )

        event_name = data.get("event_name")
        event_address = data.get("event_address")
        event_pc = data.get("event_pc")
        event_dt = data.get("event_dt")
        event_dt = datetime.strptime(event_dt, "%a, %d %b %Y %H:%M:%S %Z")
        event_details = data.get("event_details")


        event = Event.objects.create(
             event_name=event_name,
             event_address=event_address,
              event_pc=event_pc,
              event_dt=event_dt,
              event_details=event_details
        )


        return JsonResponse({"console": "Event created"})
    else:
        return JsonResponse({"message" : "something went wrong, try again"}, status=405)
