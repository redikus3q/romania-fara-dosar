from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cetatean(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CNP = models.CharField(max_length=20)
    telefon = models.CharField(max_length=20)
    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nume + " " + self.prenume

    class Meta:
        verbose_name = 'Cetatean'
        verbose_name_plural = 'Cetateni'