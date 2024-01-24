from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer


class CreateSensor(ListCreateAPIView):
    #создание датчика
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class UpdateSensor(RetrieveUpdateAPIView):
    #Изменяем датчик
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class UpdateMeaserement(ListCreateAPIView):
    #Добавляем измерения
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer