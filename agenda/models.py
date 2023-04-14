from django.db import models


class Agenda(models.Model):
    area_persona = models.CharField(verbose_name='Área/Persona',max_length=120, help_text="Área o Persona")
    numero = models.CharField(verbose_name='Número',max_length=80,help_text="Número o Extensión")
    created_at = models.DateTimeField(verbose_name='Creado',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Actualizado',auto_now=True)

    class Meta:
        ordering = ["area_persona"]
        verbose_name_plural = "Agenda"

    def __str__(self):
        return  self.area_persona

