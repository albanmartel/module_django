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
## 5.4 Exercice sur l’héritage de gabarits

### Exemple de gabarit Base

fichier __base.html__ est positionné dans le répertoire  __templates__ au même niveau que le fichier __manage.py__.

__templates\base.html__:
```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {% load static %}
    <link rel="stylesheet" href="{% static 'style.css' %}">

    <title>
        {% block title %}
        <!--
            Ce commentaire de titre dans l'onglet navigateur sera remplacé si le modèle enfant
            l'implémente. Sinon ce commentaire restera tel quel
            dans le gabarit enfant.
        -->
        {% endblock %}
    </title>
</head>
<body>
    <!-- Le titre dans la page -->
    <h1>{% block maintitle %}
        <!--
            Ce commentaire de titre dans la page sera remplacé si le modèle enfant
            l'implémente. Sinon ce commentaire restera tel quel
            dans le gabarit enfant.
        -->
        {% endblock %}
    </h1>
    <!-- La partie block Header -->
    <header>
        {% block header %}
        <!--
            Ce commentaire de header sera remplacé si le modèle enfant
            l'implémente. Sinon ce commentaire restera tel quel
            dans le gabarit enfant.
        -->
        {% endblock %}
    </header>
    <!-- La partie block Main -->
    <main>
        {% block main %}
        <!--
            Ce commentaire de main sera remplacé si le modèle enfant
            l'implémente. Sinon ce commentaire restera tel quel
            dans le gabarit enfant.
        -->
        {% endblock %}
    </main>
    <!-- La partie block Footer -->
   <footer>
       {% block footer %}
       <p>
           <a href="{% url 'polls:add' %}">Add a question</a>
       </p>
       <p>
           <a href="{% url 'polls:statistics' %}">Poll statistics</a>
       </p>
       <p>
           <a href="{% url 'polls:all' %}">All polls</a>
       </p>
       <p>
           <a href="{% url 'polls:index' %}">Home</a>
       </p>
       {% endblock %}
       </footer>
</body>
</html>
```

Note : 

### Exemple de CSS

fichier __style.css__ est positionné dans le répertoire  __static__ au même niveau que le fichier __manage.py__.

__static\style.css__:
```css
/* =========== Modèle CSS produit par Gémini AI ==============*/

/* =================================================u00e9l ==========================
   1. Variables & Reset CSS
   ========================================================================== */
:root {
    --primary-color: #4f46e5;
    --primary-hover: #4338ca;
    --secondary-color: #06b6d4;
    --bg-color: #f3f4f6;
    --card-bg: #ffffff;
    --text-main: #1f2937;
    --text-muted: #6b7280;
    --border-color: #e5e7eb;
    --success-color: #10b981;
    --danger-color: #ef4444;
    --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
    --transition: all 0.2s ease-in-out;
}

*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: var(--font-sans);
    background-color: var(--bg-color);
    color: var(--text-main);
    line-height: 1.5;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

/* ==========================================================================
   2. Layout & Navigation
   ========================================================================== */
header {
    background-color: var(--card-bg);
    border-bottom: 1px solid var(--border-color);
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-weight: 700;
    font-size: 1.25rem;
    color: var(--primary-color);
    text-decoration: none;
}

nav ul {
    display: flex;
    list-style: none;
    gap: 1.5rem;
}

nav a {
    text-decoration: none;
    color: var(--text-muted);
    font-weight: 500;
    transition: var(--transition);
}

nav a:hover {
    color: var(--primary-color);
}

main {
    flex: 1;
    max-width: 1200px;
    width: 100%;
    margin: 2rem auto;
    padding: 0 1rem;
}

/* ==========================================================================
   3. Composants UI (Cartes, Boutons, Formulaires)
   ========================================================================== */
.card {
    background-color: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 0.5rem;
    padding: 1.5rem;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    margin-bottom: 1.5rem;
}

.btn {
    display: inline-block;
    background-color: var(--primary-color);
    color: white;
    padding: 0.6rem 1.2rem;
    border-radius: 0.375rem;
    border: none;
    font-weight: 500;
    cursor: pointer;
    text-decoration: none;
    transition: var(--transition);
}

.btn:hover {
    background-color: var(--primary-hover);
}

/* Formulaires Django (Gestion des champs <input>, <select>, etc.) */
.form-group {
    margin-bottom: 1.2rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
    font-size: 0.875rem;
}

.form-group input,
.form-group select,
.form-group textarea {
    width: 100%;
    padding: 0.6rem;
    border: 1px solid var(--border-color);
    border-radius: 0.375rem;
    font-family: inherit;
    font-size: 1rem;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
}

/* ==========================================================================
   4. Messages d'alerte Django (messages framework)
   ========================================================================== */
.messages {
    list-style: none;
    margin-bottom: 1.5rem;
}

.messages li {
    padding: 0.75rem 1rem;
    border-radius: 0.375rem;
    margin-bottom: 0.5rem;
    font-size: 0.875rem;
}

.messages .success { background-color: #d1fae5; color: #065f46; }
.messages .error { background-color: #fee2e2; color: #991b1b; }
.messages .warning { background-color: #fef3c7; color: #92400e; }

/* ==========================================================================
   5. Pied de page
   ========================================================================== */
footer {
    text-align: center;
    padding: 1.5rem;
    background-color: var(--card-bg);
    border-top: 1px solid var(--border-color);
    color: var(--text-muted);
    font-size: 0.875rem;
}
```

### Réglages de Django

Pour permettre d'utiliser un répertoire __static__ racine

__Note:__ fichier __settings.py__ est positionné dans le répertoire  __mysite__ au même niveau que le fichier __manage.py__. 

_mysite_ est le nom du répertoire du site racine de djongo, il pourrait s'appeler différemment selon les cas.

__mysite\settings.css__:

```Python
...
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
...
```

Sans la directive __STATICFILES_DIRS__ django ne va pas récupérer les fichiers situés dans __racine\static__.

### Exemple d'utilisation du gabarit base dans le gabarit index


fichier __index.html__ est positionné dans le répertoire  __polls\templates\polls__. __polls__ est le répertoire site application de django au même niveau que le fichier __manage.py__.

__polls\templates\polls\index.html__:
```html
{% block title %}{{ title }}{% endblock %}

{% block maintitle %} {{ title }} {% endblock %}

{% block header %} {% endblock %}

{% block main %}

{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a> {{question.pub_date | date:"l j N Y, H:i"}}</li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}

{% endblock %}
```

