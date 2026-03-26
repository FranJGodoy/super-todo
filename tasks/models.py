from django.db import models
from django.utils.text import slugify

# Create your models here.

class Task(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    completada = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
