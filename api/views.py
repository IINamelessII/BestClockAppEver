from datetime import datetime, timedelta
from random import randint, random
from django.http import JsonResponse
from django.shortcuts import render


def state(request):
    now = datetime.now()
    start_time = datetime(now.year, now.month,
     now.day + (1 if now.hour > 6 else 0),
      6 + (1 if now.hour < 7 else 0), 0)
    data = {
        'works': random() > 0.2,
        'repeat_counter': randint(0, 10),
        'alert_time':  (start_time + timedelta(minutes=randint(0, 60))).strftime('%Y-%m-%d %H:%M'),
        'power_from_network': random() > 0.5,
    }
    return JsonResponse(data)