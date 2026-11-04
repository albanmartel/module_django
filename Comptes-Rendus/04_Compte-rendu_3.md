# Compte rendu Exercice 3

## Evolution du fichier _polls/views.py_

### origine 

A l'origine : le fichier ressemble à ceci

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```



### Ecriture de vues supplémentaires

<https://docs.djangoproject.com/fr/5.2/intro/tutorial03/#writing-more-views>

1.  mise à jour du fichier _polls/views.py_
2.  mise à jour du fichier _polls.urls_ pour ajouter  des appels __path()__

### Écriture de vues qui font réellement des choses

#### Un raccourci : render()

1.  mise à jour du fichier _polls/views.py_
 
### Les erreurs 404

1. mise à jour du fichier _polls/views.py_
2. Création d'un gabarit(template) _polls/detail.html_

#### Optimisation de la gestion d'exception avec : __get_object_or_404()__

1. mise à jour du fichier _polls/views.py_ avec optimisation du code en utilisant un raccourci __get_object_or_404()__

### Utilisation du système de gabarits

### Suppression des URL codés en dur dans les gabarits

### Espaces de noms et noms d’URL

