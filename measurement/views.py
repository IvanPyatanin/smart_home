from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, SensorSerializer, MeasurementSerializer


class CreateSensor(ListAPIView):
    #создание датчика
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        review = SensorSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response({'status': 'ok'})

class UpdateSensor(RetrieveAPIView):
    #Изменяем датчик
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        serializer = SensorSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

class UpdateMeaserement(RetrieveAPIView):
    #Добавляем измерения
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request, pk):
        measurement = Measurement.object.get(pk=pk)
        serializer = MeasurementSerializer(measurement, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

class AllListSenson(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer