from rest_framework import serializers

from data.models import StateData

class StateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateData
        fields = '__all__'