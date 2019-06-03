from django.urls import path
from api import views


urlpatterns = [
    path('state', views.state, name='state'),
    path('update_data', views.update_state, name='update-data'),
    path('randomize', views.randomize_data, name='randomize'),
]
