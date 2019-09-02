from django.db import models
from django.utils import timezone

class Course(models.Model):
    exp_nom = models.CharField(max_length=100,verbose_name="Nom expéditeur")
    exp_tel = models.CharField(max_length=10,verbose_name="Téléphone expéditeur")
    dest_nom = models.CharField(max_length=100,verbose_name="Nom destinataire")
    dest_tel = models.CharField(max_length=10,verbose_name="Téléphone destinataire")
    dest_adresse = models.CharField(max_length=100,verbose_name="Adresse destination")
    dest_colis = models.TextField(max_length=250,verbose_name="Description du service")
    date = models.DateTimeField(default=timezone.now, verbose_name="Date enregistrement")
    livreur = models.ForeignKey('Livreur',null=True, on_delete=models.SET_NULL)
    
    class Meta:
        verbose_name = "course"
        ordering = ['date']
    
    def __str__(self):

        return self.exp_nom


class Livreur(models.Model):
    nom = models.CharField(max_length=100)

    
    class Meta:
        verbose_name = "livreur"

    
    def __str__(self):

        return self.nom