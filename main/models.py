from django.db import models
from django.contrib.auth.models import User
from authentication.models import Cetatean


# Create your models here.
class Buletin(models.Model):
    cetatean = models.ForeignKey(Cetatean, on_delete=models.RESTRICT)
    CNP = models.CharField(max_length=20)
    serie = models.CharField(max_length=20)
    numar = models.CharField(max_length=50)
    cetatenie = models.CharField(max_length=50)
    loc_nastere = models.CharField(max_length=100)
    domiciliu = models.CharField(max_length=100)
    autoritate_emitenta = models.CharField(max_length=100)
    data_emitere = models.DateField()
    data_expirare = models.DateField()
    link_descarcare_document = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.serie + self.numar

    class Meta:
        verbose_name = 'Buletin'
        verbose_name_plural = 'Buletine'


class CertificatInregistrarePFA(models.Model):

    cetatean = models.ForeignKey(Cetatean, on_delete=models.RESTRICT)
    nume_firma = models.CharField(max_length=100)
    cod_CAEN = models.CharField(max_length=20)
    sediu_profesional = models.CharField(max_length=100)
    CUI = models.CharField(max_length=20)
    EUID = models.CharField(max_length=20)
    numar_de_ordine_ONRC = models.CharField(max_length=20)
    serie = models.CharField(max_length=20)
    numar = models.CharField(max_length=20)
    data_eliberare = models.DateField()
    link_descarcare_document = models.CharField(max_length=100)

    def __str__(self) -> str:
        return "PFA - " + self.nume_firma

    class Meta:
        verbose_name = 'Certificat Inregistrare PFA'
        verbose_name_plural = 'Certificate Inregistrare PFA'


class CertificatHandicap(models.Model):

    class GradHandicap(models.TextChoices):
        USOR = 'Usor'
        MEDIU = 'Mediu'
        ACCENTUAT = 'Accentuat'
        GRAV_CU_ASISTENT_PERSONAL = 'Grav cu asistent personal'
        GRAV = 'Grav'

    class TipHandicap(models.TextChoices):
        FIZIC = "Fizic"
        VIZUAL = "Vizual"
        AUDITIV = "Auditiv"
        SURDOCECITATE = "Surdocecitate"
        SOMATIC = 'Somatic'
        MINTAL = 'Mintal'
        PSIHIC = 'Psihic'
        HIV_SIDA = 'HIV/SIDA'
        ASOCIAT = 'Asociat'
        BOLI_RARE = 'Boli rare'

    cetatean = models.ForeignKey(Cetatean, on_delete=models.RESTRICT)
    grad_handicap = models.CharField(
        max_length=50,
        choices=GradHandicap.choices,
    )
    tip_handicap = models.CharField(
        max_length=50,
        choices=TipHandicap.choices,
    )
    link_descarcare_document = models.CharField(max_length=100)

    def __str__(self) -> str:
        return "Certificat Handicap - " + self.cetatean.nume + " " + self.cetatean.prenume

    class Meta:
        verbose_name = 'Certificat Handicap'
        verbose_name_plural = 'Certificate Handicap'