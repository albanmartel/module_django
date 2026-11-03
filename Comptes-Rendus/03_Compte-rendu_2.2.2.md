# Compte rendu Exercice 2.2.2

```python
Question.objects.all()

\djangotutorial> python manage.py shell
8 objects imported automatically (use -v 2 for details).

Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> Question.objects.all()
<QuerySet [<Question: Qu'y a-t-il de nouveau aujourd'hui ?>, <Question: Faut-il relancer des voyages spatiaux sur la  lune>, <Question: La publication des sondages dans la presse influence t-elle notre opinion ?>, <Question: Quel est votre moment préféré de la journée ?>, <Question: Quel type de sortie préférez-vous ?>]>
>>>
```

## 1. boucle for

```python
>>> for elem in questions:
...     print(elem)
...
Qu'y a-t-il de nouveau aujourd'hui ?
Faut-il relancer des voyages spatiaux sur la  lune
La publication des sondages dans la presse influence t-elle notre opinion ?
Quel est votre moment préféré de la journée ?
Quel type de sortie préférez-vous ?
>>>
```

## 2. Filtrer par année et mois

```Python
>>> Question.objects.filter(pub_date__year=2026, pub_date__month=11)
<QuerySet [<Question: Faut-il relancer des voyages spatiaux sur la  lune>, <Question: La publication des sondages dans la presse influence t-elle notre opinion ?>]>
>>>
```

```python
>>> Question.objects.filter(pub_date__year=2026, pub_date__month=11, pub_date__day=2)
<QuerySet [<Question: Faut-il relancer des voyages spatiaux sur la  lune>]>
>>>
```

## 3. Trouver la seconde question à partir de son id, afficher les attributs et l'ensemble des choix de la question.

```Python
>>> i = 1
>>> question = Question.objects.get(pk=2)
>>> print(f"id:{question.id}, question_text: {question.question_text}, pub_date: {question.pub_date}.")
id:2, question_text: Faut-il relancer des voyages spatiaux sur la  lune, pub_date: 2026-11-02 08:33:47+00:00.
>>> for choice in question.choice_set.all():
...     print(choice.choice_text)
...
Oui, c'est une bonne chose
Non, cela n'a plus d'intérêt scientifique
Je n'ai pas d'opinion sur la question.
>>>
```

## 4. Faire une boucle pour afficher les attribus de chaque question et leurs choix associés

```python
>>> for question in Question.objects.all():
...     print(f"Question n°{i}")
...     print("===========================")
...     print(f"id:{question.id}, question_text: {question.question_text}, pub_date: {question.pub_date}.")
...     for choice in question.choice_set.all():
...             print(choice.choice_text)
...     i +=1
...     print()
...
Question n°1
===========================
id:1, question_text: Qu'y a-t-il de nouveau aujourd'hui ?, pub_date: 2026-10-30 08:51:20+00:00.
Rien de nouveau
Le temps
C'est l'anniversaire d'une date historique
Quelqu'un d'important est mort
Il y a un heureux évènement

Question n°2
===========================
id:2, question_text: Faut-il relancer des voyages spatiaux sur la  lune, pub_date: 2026-11-02 08:33:47+00:00.
Oui, c'est une bonne chose
Non, cela n'a plus d'intérêt scientifique
Je n'ai pas d'opinion sur la question.

Question n°3
===========================
id:3, question_text: La publication des sondages dans la presse influence t-elle notre opinion ?, pub_date: 2026-11-03 08:39:26+00:00.
Oui, nettement
Non, nous y sommes tellement habitués
Cela influence les résultats électoraux
Uniquement sur les personnes indécises

Question n°4
===========================
id:4, question_text: Quel est votre moment préféré de la journée ?, pub_date: 2026-10-26 14:22:00+00:00.
le matin
L'après-midi
Le soir
La nuit

Question n°5
===========================
id:5, question_text: Quel type de sortie préférez-vous ?, pub_date: 2026-10-27 08:47:21+00:00.
Un repas au restaurant
Une activité en plein air
Une soirée cinéma
Une sortie culturelle
Regarder la TV à la maison

>>>
```

## 5. Affichez le nombre de choix enregistrés pour chaque question.

```python
>>> i = 1
>>> for question in Question.objects.all():
...     print(f"Pour la question n°{i}, il y a {question.choice_set.count()} choix.")
...     i += 1
...
Pour la question n°1, il y a 5 choix.
Pour la question n°2, il y a 3 choix.
Pour la question n°3, il y a 4 choix.
Pour la question n°4, il y a 4 choix.
Pour la question n°5, il y a 5 choix.
>>>
```

## 7. Triez les questions par ordre antéchronologique.

```python
>>> print("Triez les questions par ordre antéchronologique.")
Triez les questions par ordre antéchronologique.
>>> for question in Question.objects.order_by("-pub_date"):
...     print(f"Question: \"{question.question_text}\" publié le: \"{question.pub_date.year}-{question.pub_date.month}-{question.pub_date.day}\"")
...
Question: "La publication des sondages dans la presse influence t-elle notre opinion ?" publié le: "2026-11-3"
Question: "Faut-il relancer des voyages spatiaux sur la  lune" publié le: "2026-11-2"
Question: "Qu'y a-t-il de nouveau aujourd'hui ?" publié le: "2026-10-30"
Question: "Quel type de sortie préférez-vous ?" publié le: "2026-10-27"
Question: "Quel est votre moment préféré de la journée ?" publié le: "2026-10-26"
>>>
```

## 9. Créez une question en utilisant le shell

```python
print("Créez une question en utilisant le shell.")
>>> print("la méthode vient de https://docs.djangoproject.com/fr/5.2/intro/tutorial02/")
la méthode vient de https://docs.djangoproject.com/fr/5.2/intro/tutorial02/
>>> question = Question(question_text="Aimez-vous le chocolat ?", pub_date=timezone.now())
>>> print("Afficher l'id de la question")
Afficher l'id de la question
>>> print(question.id)
None
>>> print("Sauvegarder la question dans la base de données SQLite")
Sauvegarder la question dans la base de données SQLite
>>> question.save()
>>> choix = Choice(choice_text="Je déteste ça",question_id=question.id)
>>> choix.save()
>>> choix = Choice(choice_text="Le chocolat, c'est une passion !",question_id=question.id)
>>> choix.save()
>>> choix = Choice(choice_text="Je n'aime que le chocolat au lait",question_id=question.id)
>>> choix.save()
>>> choix = Choice(choice_text="Le chocolat, je peux tout à fait m'en passer !",question_id=question.id)
>>> choix.save()
>>>
```