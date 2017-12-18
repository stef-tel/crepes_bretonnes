from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect 
from datetime import datetime
from blog.models import Article

def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})

def whoami(request):
    return render(request, 'blog/testBoostrap.html', locals())


def addition(request, nombre1, nombre2):    
    total = int(nombre1) + int(nombre2)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())

def couleurs(request):    
    couleurs = {'FF0000':'rouge', 
            'ED7F10':'orange', 
            'FFFF00':'jaune', 
            '00FF00':'vert', 
            '0000FF':'bleu', 
            '4B0082':'indigo', 
            '660099':'violet'}

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/couleurs.html', locals())

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})



def lire(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/lire.html', {'article':article})


from blog.forms import ContactForm

def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données 
        # que nous venons de récupérer
        envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'blog/contact.html', locals())

from blog.forms import ArticleForm

def addArticle(request):
    #article = {
    #            'titre':"Les crêpes c'est trop bon",
    #            'auteur':"Maxime",
    #            'contenu':"Vous saviez que les crêpes bretonnes c'est trop bon ? La pêche c'est nul à côté.",
    #            'categorie':" # Nous prenons l'identifiant de la première catégorie qui vient
    #            }

    #form = ArticleForm(request.POST or none)  # instance=article, article est bien entendu un objet d'Article quelconque dans la base de données
    
    if request.method == "POST":
        form = ArticleForm(request.POST or none)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('article/' + str(post.id))
    else:
        form = ArticleForm()  

    return render(request, 'blog/addArticle.html', {'form': form})
    #return render_to_response('blog/addArticle.html',
    #                            locals(),
    #                            context_instance_=requestContext(request))

