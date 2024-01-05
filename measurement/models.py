from django.db import models

# Create your models here.
class Sensor(models.Model):

    name = models.CharField(max_length=100, verbose_name='датчик')
    description = models.CharField(max_length=100, verbose_name='описание')

    class Meta:
        ordering = ['-id']

class Measurement(models.Model):

    temperature = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='температура')
    data_time = models.DateTimeField(auto_now=True, verbose_name='дата и время')
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')

    class Meta:
        ordering = ['-sensor_id']