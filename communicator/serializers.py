from .models import Device
from rest_framework import serializers


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'slug', 'status']
