from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from api.models import State


def randomize_data(request):
    try:
        State.randomize(State)
    except:
        return HttpResponse(status=404)
    else:
        return HttpResponse(status=200)


def update_state(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        State.update_data(State, data)
    except:
        return HttpResponse(status=404)
    else:
        return HttpResponse(status=200)
        

def state(request):
    return JsonResponse(State.get_last(State))