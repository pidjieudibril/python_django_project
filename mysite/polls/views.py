from django.shortcuts import render,get_object_or_404

from .models import Person, Post # import the models from polls/models.py
def index (request):
    return render(request, 'homepage.html')
# afficher une personne 

def afficher_personne(request, personne_id):
    personne = get_object_or_404(Person, pk=personne_id)
    return render(request, 'personne.html', {'personne': personne})

# afficher toutes les personne 
def afficher_toutes_personnes(request):
    personnes = Person.objects.all()
    return render(request, 'all_personne.html', {'personnes': personnes})

#afficher publication 
def afficher_publication(request, publication_id):
    publication = get_object_or_404(Post, pk=publication_id)
    return render(request, 'posts.html', {'publication': publication})

#afficher toutes les publication 
def afficher_toutes_publications(request):
    publications = Post.objects.all()
    return render(request, 'all_posts.html', {'publications': publications})