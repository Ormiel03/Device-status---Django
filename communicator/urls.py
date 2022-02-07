from django.urls import path
from . import views

from rest_framework import routers
from django.urls import include, path
from .views import DeviceViewSet

router = routers.DefaultRouter()
router.register('Device', DeviceViewSet)

app_name = 'communicator'

urlpatterns = [
     path('api/', include(router.urls)),
     path('', views.device_list, name='devices'),

    ]



# app_name = 'communicator'
#
#  urlpatterns = [
#      path('', views.device_list, name='devices'),
#  ]
