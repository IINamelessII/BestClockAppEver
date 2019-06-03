from django.shortcuts import render
from api.models import State


def index(request):
    state = State.get_last(State)
    return render(request, 'main/index.html', state)
