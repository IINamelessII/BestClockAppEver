from django.urls import path
from api import views


urlpatterns = [
    path('state', views.state, name='state'),
]
