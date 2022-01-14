from django.db import models

# Create your models here.

class City (models.Model):
    name_city = models.CharField(max_length=20)

    def __str__(self):
        return self.name_city

    class Meta:
        verbose_name_plural = 'cities'
