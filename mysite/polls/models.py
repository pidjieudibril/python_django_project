from django.db import models

# Create your models here.
from datetime import datetime, date


class Person(models.Model):
    prenom = models.CharField(max_length=30)  # Prénom de la personne
    nom_de_famille = models.CharField(max_length=40)  # Nom de famille de la personne
    date_de_naissance = models.DateField()  # Date de naissance de la personne
    a_un_animal_de_compagnie = models.BooleanField(default=True)  # Indique si la personne a un animal de compagnie
    official_homepage = models.fields.URLField(null=True, blank=True) #blank=True ici nous permettra de soumettre ce formulaire avec une zone de texte vide pour ce champ.


class Post(models.Model):
    class PostType (models.TextChoices):
        JOURNAL = 'J'
        TECHNOLOGIE = 'T'
        POLITIQUE = 'P'
        ECONOMIQUE = 'E'


    titre = models.CharField(max_length=100)  # Titre du post
    texte = models.TextField()  # Texte du post
    categorie = models.CharField(max_length=50)  # Catégorie du post
    date_de_publication = models.DateField(default=datetime.now())  # Date de publication du post
    type= models.fields.CharField(choices=PostType.choices, max_length=10)
    auteur = models.ForeignKey(Person, on_delete=models.CASCADE)  # Auteur du post (relation avec la classe Person)
    # Si on supprime une personne, ses posts seront également supprimés


    def __str__(self):
        return f'{self.title}'
    