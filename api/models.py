from datetime import datetime, timedelta
from random import randint, random
from django.db import models
from django.utils.timezone import now


class State(models.Model):
    works = models.BooleanField(default=True)
    repeat_counter = models.PositiveIntegerField()
    alert_time = models.DateTimeField(default=now)
    power_from_network = models.BooleanField(default=True)

    def __str__(self):
        return 'State data #' + self.id
    
    def update_data(self, data):
        state = State(
            works=data['works'],
            repeat_counter=data['repeat_counter'],
            alert_time=data['alert_time'],
            power_from_network=data['power_from_network']
        )
        state.save()
        try:
            State.objects.all().order_by('-id')[1].delete()
        except:
            pass

    def get_last(self):
        state = State.objects.all().order_by('-id')[0]
        data = {
            'id': state.id,
            'works': state.works,
            'repeat_counter': state.repeat_counter,
            'alert_time': state.alert_time,
            'power_from_network': state.power_from_network,
        }
        return data
    
    def randomize(self):
        now = datetime.now()
        start_time = datetime(now.year, now.month,
        now.day + (1 if now.hour > 6 else 0),
        6 + (1 if now.hour == 6 else 0), 0)
        data = {
            'works': random() > 0.2,
            'repeat_counter': randint(0, 10),
            'alert_time': start_time + timedelta(minutes=randint(0, 60)),
            'power_from_network': random() > 0.5,
        }
        State.update_data(self, data)