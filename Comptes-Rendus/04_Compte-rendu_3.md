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
2. Création d'un gabarit(template) _polls/templates/polls/detail.html_

#### Optimisation de la gestion d'exception avec : __get_object_or_404()__

1. mise à jour du fichier _polls/templates/polls/views.py_ avec optimisation du code en utilisant un raccourci __get_object_or_404()__

### Utilisation du système de gabarits

Les gabarits sont rangés dans : _polls/templates/polls_

__boucle for dans une page html :__
```html
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
```

### Suppression des URL codés en dur dans les gabarits

Remplacer les url en dur par url dynamique.

### Espaces de noms et noms d’URL

code pour avoir un espace de nom:

```html
app_name = "polls"
```

### 3.2 Exercice sur les parties 3 et 4

#### 3.2.1  Affichage de la date de publication

```html
{{question.pub_date | date:"l j N Y, H:i"}}
```

#### 3.2.2 Ajouter une page all qui liste les sondages

```html
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a> id : {{question.id}}, créé le: {{question.pub_date | date:"l j N Y, H:i"}}</li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}

<a href="{% url 'polls:index' %}">Retour à l'index </a>
```

#### 3.2.3 Ajouter une page frequency pour afficher les resultats des votes en valeur absolus.

1. Création __djangotutorial\polls\templates\polls\frequency.html__

_solution présentée par Mathieu Rocamcourt_

```html
<h1>{{ question.question_text }}</h1>

<ul>
    {% for choice in question.get_choices %}
    <li>{{ choice.0 }}: {{ choice.1 }} vote{{ choice.1|pluralize }}, fréquence: {{ choice.2|floatformat:"2" }} %</li>
    {% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```

2. Mise à jour __djangotutorial\polls\urls.py__
```html
    # ex /polls/1/frequency
    path("<int:pk>/frequency", views.FrequencyView.as_view(), name="frequency"),
```

2. Mise à jour __djangotutorial\polls\views.py__
```html
class FrequencyView(generic.DetailView):
    model = Question
    template_name = "polls/frequency.html"
    context_object_name = "question"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["frequencies"] = self.object.get_choices()
        return context
```
