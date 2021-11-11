#Python
from django.http.response import HttpResponse

#Utilities
from datetime import datetime
import json

def hello_world(request):
    date: datetime = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Hello, World {date}')

def sorted_integers(request):
    numbers = sorted([int(i) for i in request.GET['numbers'].split(',')])
    json_response = {
        'results': numbers,
        'message': 'The response was succesfully.'
    }
    return HttpResponse(
        json.dumps(json_response, indent=4), 
        content_type="application/json"
    )

def validate_age(request,name,age):
    message: str
    if age >12:
        message = 'You are inside, Hi {}'.format(name)
    else:
        message = 'You are outside, Hi {}'.format(name)
    return HttpResponse(message)