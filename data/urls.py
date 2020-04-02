from django.urls import path
from data.views import index, state_data

urlpatterns = [
    path('', index, name='index'),
    path('state-data/', state_data, name='state_data'),   
]