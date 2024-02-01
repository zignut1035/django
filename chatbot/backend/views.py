from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def backend(request, slug=None):
    return HttpResponse("<p>Hello from the backend-side</p>")
import json
from . responses import bot_response

import requests
last_message = ""
def get_chat_response(request, slug = None):
    global last_message
    data = request.GET
    message = data.get("message")
    response = {
        "message": bot_response(message)
    }
    return HttpResponse(json.dumps(response))
def first_message(response, slug = None):
    
    response = {
        "message": "Hello there!"
    }
    return HttpResponse(json.dumps(response))

import random

def get_random_image_url(request, slug = None):
    data = request.GET
    message = data.get("https://picsum.photos/200/300/?id=" + str(random.randint(1, 1000)))
    response = {
        "message": bot_response(message)
    }
    return HttpResponse(json.dumps(response))

def get_wikipedia(request, slug = None):
    something = request[3]
    data = request.GET
    message = data.get(f"https://en.wikipedia.org/wiki/{something}")
    response = {
        "message": bot_response(message)
    }
    return HttpResponse(json.dumps(response))



def get_weather(request, slug = None):
    city = request[2]
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=59cbfb7e1ab794582f5c92629bbfc890&units=metric"
    data = request.GET
    message = data.get(url)
    response = {
        "message": bot_response(message)
    }
    return HttpResponse(json.dumps(response))

