from django.db import models

# Create your models here.
class Areas(models.Model):
    nombre = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Areas"

    def __str__(self):
        return self.nombre


class Asunto(models.Model):
    categoria = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["categoria"]
        verbose_name_plural = "Asuntos"

    def __str__(self):
        return self.categoria

class Registro(models.Model):
    area = models.ForeignKey(Areas, on_delete=models.CASCADE)
    asunto = models.ForeignKey(Asunto, on_delete=models.CASCADE)
    registro = models.CharField(max_length=250,help_text="Descripción del registro")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Registros"

    
    def __str__(self):
        return self.registro


