from django.shortcuts import render
from django.http import JsonResponse
import json


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
