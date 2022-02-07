from django.shortcuts import render
from .models import Device
from rest_framework import viewsets
from .serializers import DeviceSerializer



class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer



def device_list(request):

    context = {}
    context["dataset"] = Device.objects.all()

    return render(request, 'communicator/list.html', context)
