from django.db import models
from .choices import EXAM_CHOICES, CHOICES_SEDES, NP


# Create your models here.


class Data(models.Model):
    run = models.CharField("RUN", max_length=10, primary_key=True)
    nombre = models.CharField("Nombre", max_length=255)
    exam = models.CharField("Examen", max_length=20, choices=EXAM_CHOICES)
    fecha = models.DateField("Fecha")
    hora_inicio = models.CharField("Hora Inicio", max_length=5)
    hora_fin = models.CharField("Hora Fin", max_length=5)
    sala = models.CharField("Sala", max_length=20)
    proctor = models.CharField("Proctor", max_length=255)
    sede = models.CharField("Sede", max_length=255, choices=CHOICES_SEDES, default=NP)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    # META CLASS
    class Meta:
        verbose_name = "Data"
        verbose_name_plural = "Datos"
        ordering = ["-fecha"]

    # TO STRING METHOD
    def __str__(self):
        return 'Examen: {0} - Fecha: {1} - Hora Inicio {2} - Fin {3} - Sala {4} - Proctor {5}'.format(self.exam,
                                                                                                      self.fecha,
                                                                                                      self.hora_inicio,
                                                                                                      self.hora_fin,
                                                                                                      self.sala,
                                                                                                      self.proctor)


class StarRating(models.Model):
    run = models.CharField("RUN_alumno", max_length=12)
    rating_value  = models.SmallIntegerField("rating", null=True, blank=True, default=0)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    # META CLASS
    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"
        ordering = ["-created"]

    # TO STRING METHOD
    def __str__(self):
        return 'Run: {0} - Rating: {1}'.format(self.run, self.rating_value)

