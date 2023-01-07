from django.db import models
from datetime import date

class Todo(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(max_length=200, blank=False, null=False)
    fecha = models.DateField(default=date.today)
    fechaFinalizacion = models.DateField(blank=False, null=False)
    prioridad = models.IntegerField(default=3)

    def __str__(self):
        return self.titulo


