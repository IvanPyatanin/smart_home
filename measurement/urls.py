from django.urls import path

from measurement.views import CreateSensor, UpdateSensor, UpdateMeaserement, AllListSenson

urlpatterns = [
    path('sensor/', CreateSensor.as_view()),
    path('sensor/<pk>/', UpdateSensor.as_view()),
    path('measurements/<pk>', UpdateMeaserement.as_view()),
    path('list/', AllListSenson.as_view()),
]