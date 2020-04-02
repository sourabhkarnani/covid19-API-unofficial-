from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from data.scrapper import get_state_data
from data.serializers import StateDataSerializer
from data.models import StateData

@api_view(['GET'])
def index(request):
    done = get_state_data()
    if done:
        return Response({'status': 'success'})
    else:
        return Response({'status':'error'})

@api_view(['GET'])
def state_data(request):
    try:
        state_data = StateData.objects.all()
        serializer  = StateDataSerializer(state_data, many=True)
        return Response({'status':'success', 'data':serializer.data})
    except:
        return Response({'status':'error', 'message':str(e)})