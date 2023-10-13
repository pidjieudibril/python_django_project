from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('', views.index, name='index'),
     # URL pour afficher toutes les personnes
    path('personnes/', views.afficher_toutes_personnes, name='afficher_toutes_personnes'),

    # URL pour afficher une personne en fonction de son ID
    path('personnes/<int:personne_id>/', views.afficher_personne, name='afficher_personne'),

    # URL pour afficher toutes les publications
    path('publications/', views.afficher_toutes_publications, name='afficher_toutes_publications'),

    # URL pour afficher une publication en fonction de son ID
    path('publications/<int:publication_id>/', views.afficher_publication, name='afficher_publication'),

]