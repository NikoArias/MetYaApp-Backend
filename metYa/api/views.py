from django.shortcuts import render
from django.http import JsonResponse
import json
import jwt
from datetime import datetime
from .models import Event
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from metYa.settings import SECRET_KEY

from django.core.paginator import Paginator


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

def login_endpoint(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")



        user = authenticate(request, username=username, password=password)
        if user is None:
            return JsonResponse({
                "msg": "username or password is incorrect",
            }, status=401)



        login(request, user)



        encoded_jwt = jwt.encode({"user_id": user.id}, SECRET_KEY, algorithm="HS256")



        return JsonResponse({
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "token": encoded_jwt,
        })

    else:
        return JsonResponse({
            "msg": "method not allowed",
        }, status=405)

def register_endpoint(request):
    if request.method == "POST":
        data = json.loads(request.body)
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")




        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()



        return JsonResponse({
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
        })
    else:
        return JsonResponse({
        "msg": "method not allowed",
        }, status=405)


def list_create_event_api_endpoint(request):
    if request.method == "GET":
        events = Event.objects.all()
        events_count = Event.objects.count()

        limit_numb = request.GET.get("limit", 25)
        paginator = Paginator(events, limit_numb)
        page_numb = request.GET.get("page", 1)

        page_obj = paginator.get_page(page_numb)

        results = []
        for event in page_obj:
            r = {
                "id": event.id,
                "event_host": event.event_host,
                "event_name": event.event_name,
                "event_address": event.event_address,
                "event_pc": event.event_pc,
                "event_dt": event.event_dt,
                "event_details": event.event_details,
                "event_long": event.event_long,
                "event_lat": event.event_lat,
                "event_img": event.event_img,

            }
            results.append(r)

        return JsonResponse({
            "count": events_count,
            "results": results,
        })

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"msg":"Fill the forms"}, status=400 )

        event_name = data.get("event_name")
        event_host = data.get("event_host")
        event_address = data.get("event_address")
        event_pc = data.get("event_pc")
        event_dt = data.get("event_dt")
        event_dt = datetime.strptime(event_dt, "%a, %d %b %Y %H:%M:%S %Z")
        event_details = data.get("event_details")
        event_lat = data.get("event_lat")
        event_long= data.get("event_long")
        event_img = data.get("event_img")


        event = Event.objects.create(
              event_host = event_host,
              event_name = event_name,
              event_address = event_address,
              event_pc = event_pc,
              event_dt = event_dt,
              event_details = event_details,
              event_lat = event_lat,
              event_long = event_long,
              event_img = event_img,
        )


        return JsonResponse({"console": "Event created"})
    else:
        return JsonResponse({"message" : "something went wrong, try again"}, status=405)

def retrieve_update_delete_event_endpoint(request,id):
    print("---------------------------------------------------------------------------------------------------")
    try:
        event = event.objects.get(id=id)
    except event.DoesNotExist:
        return JsonResponse({"error":"d.n.e."},status=404)


    if request.method == "GET": # Details
        # "Serialization"
        response = {
            "id": event.id,
            "event_host": event.event_host,
            "event_name": event.event_name,
            "event_address": event.event_address,
            "event_pc": event.event_pc,
            "event_dt": event.event_dt,
            "event_details": event.event_details,
            "event_long": event.event_long,
            "event_lat": event.event_lat,
            "event_img": event.event_img,
        }
        return JsonResponse(response, status=200)

    elif request.method == "PUT": # Update
        data = json.loads(request.body)

        event_name = data.get("event_name")
        event_host = data.get("event_host")
        event_address = data.get("event_address")
        event_pc = data.get("event_pc")
        event_dt = data.get("event_dt")
        event_dt = datetime.strptime(event_dt, "%a, %d %b %Y %H:%M:%S %Z")
        event_details = data.get("event_details")
        event_lat = data.get("event_lat")
        event_long= data.get("event_long")
        event_img = data.get("event_img")


        event.event_name = event_name
        event.event_host = event_host
        event.event_address = event_address
        event.event_pc = event_pc
        event.event_dt = event_dt
        event.event_details = event_details
        event.event_lat = event_lat
        event.event_long = event_long
        event.event_img = event_img
        event.save()

        # "Serialization"
        response = {
            "id": event.id,
            "event_host": event.event_host,
            "event_name": event.event_name,
            "event_address": event.event_address,
            "event_pc": event.event_pc,
            "event_dt": event.event_dt,
            "event_details": event.event_details,
            "event_long": event.event_long,
            "event_lat": event.event_lat,
            "event_img": event.event_img,
        }
        return JsonResponse(response, status=200)

    elif request.method == "DELETE": # Delete
        event.delete()
        return JsonResponse({}, status=204)
    else:
        return JsonResponse({
            "msg": "method not allowed",
        }, status=405)

def create_user_profile_endpoint(request):
    if request.method == "POST":
        data = json.loads(request.body)



        user_f_name = data.get("first name")
        user_l_name = data.get("last name")
        user_descrip = data.get("Description")
        f_link = data.get("facebook url")
        t_link = data.get("twitter url")
        i_link = data.get("instagram url")
        s_link = data.get("snapchat url")




        return JsonResponse({
            "msg": "Welcome " + name,
        })
    else:
        return JsonResponse({
            "msg": "crappy method",
        }, status=405)
