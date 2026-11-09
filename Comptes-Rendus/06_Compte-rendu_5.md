# Partie 5

## 5.1 FORMULAIRES

### Création d'un formulaire 

#### 1. Créer le modèle de formulaire
Enregistrer dans le fichier __form.py__, s'il n'existe pas le créer.

```python
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
```

#### 2. Faire le routage de la vue du formulaire

Enregistrer dans le fichier __urls.py__ :

```python
from django.urls import path, include

from . import views

    # ex /polls/contacts
    path('contact/', views.get_name, name='get_name'),
```

#### 3. Créer une vue 

Enregistrer dans le fichier __views.py__ :

la variable NameForm est récupérée dans le fichier __form.py__.

```python

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .forms import NameForm

def get_name(request):
  # Si c'est un POST, on passe les données. Si c'est un GET, request.POST est vide donc vaut None (formulaire vide)
  form = NameForm(request.POST or None)

  # Si la méthode est POST et que le formulaire est valide
  if request.method == "POST" and form.is_valid():
    name = form.cleaned_data["your_name"]
    request.session["submitted_name"] = name
    return HttpResponseRedirect("/polls/thanks/")

  # Dans tous les autres cas (GET initial ou POST invalide), on affiche le formulaire
  return render(request, "polls/name.html", {"form": form})
 
   return render(request, "polls/name.html", {"form": form})
```

_Quand le formulaire est validé, il y a une redirection, ici c'est __polls/thanks__

#### 4. Créer 2 gabarits 

##### 4.1 Le premier est pour la page où s'affiche le formulaire: 

Enregistrer dans une nouvelle template (Gabarit) __/polls/template/polls/name.html__
```html
<form action="/polls/contact/" method="post">
    <!-- Jeton de sécurité obligatoire pour les requêtes POST en Django -->
    {% csrf_token %}

    <!-- Affiche les champs du formulaire générés automatiquement -->
    {{ form }}

    <input type="submit" value="Envoyer">
</form>
```

##### 4.2 Le second est pour le traitement du formulaire: 


__polls/thanks/__ est _l'url ooù sera redirigé l'utilisateur dès qu'il aura validé le formulaire._

```html
<h1>Merci {{ name }} !</h1>
<p>Votre formulaire a bien été pris en compte.</p>
```

### Traitement d'un formulaire

#### 1. Faire le routage de la page de traitement du formulaire

Enregistrer dans le fichier __urls.py__ :

```python
from django.urls import path, include

from . import views

    # ex /polls/thanks
    path("thanks/", views.thanks_view, name="thanks"),
```

#### 2. Créer une vue utilisatrice du gabarit __polls/thanks.html__

__views.py__

```python
from django.shortcuts import get_object_or_404, render

 def thanks_view(request):
     # On récupère le nom depuis la session (avec une valeur par défaut si vide)
     name = request.session.get("submitted_name", "invité")
 
     return render(request, "polls/thanks.html", {"name": name})
```

#### 2. Créer un gabarit __polls/thanks.html__

```html
<h1>Merci {{ name }} !</h1>
<p>Votre formulaire a bien été pris en compte.</p>
```



