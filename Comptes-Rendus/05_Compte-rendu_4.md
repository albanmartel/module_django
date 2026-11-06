# Partie 4

## 4.1

### 4.1.1 Écriture de votre première application Django, 5e partie [optionnel]

__Résumé de la partie optionnel__ (généré avec IA gemini)

Voici une synthèse de la **cinquième partie du tutoriel officiel de Django**, dédiée aux **tests automatisés** (`[https://docs.djangoproject.com/fr/5.2/intro/tutorial05/](https://docs.djangoproject.com/fr/5.2/intro/tutorial05/)`).

### 1. Pourquoi des tests automatisés ?

* **Gagner du temps :** Les tests vérifient automatiquement le comportement de votre application à votre place.
* **Sécurité lors des modifications :** Si vous modifiez du code plus tard, les tests vous garantissent que vous n'avez rien cassé (*régression*).
* **Confiance :** Un code testé est un code robuste, prêt pour la production.

### 2. Le principe (TDD / Approche Django)

Django intègre un framework de test basé sur le module standard `unittest` de Python.

* Les tests s'exécutent dans une **base de données de test temporaire** distincte de votre vraie base de données.
* Pour lancer les tests, on utilise la commande :
```bash
python manage.py test
```
### 3. Écrire son premier test (Tester un modèle) 

Le tutoriel montre comment tester le comportement d'un modèle (par exemple, la méthode `was_published_recently()` d'une question).

* **Où les écrire :** Dans le fichier `tests.py` de votre application `polls`.
* **Exemple de test :** On crée une classe qui hérite de `TestCase` et on écrit des méthodes de test commençant par le préfixe `test_`.
```python
import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recent() retourne False pour les questions
        dont la date de publication est dans le futur.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```
### 4. Tester les vues (L'outil de test Client)

Django fournit un **Client de test** (`self.client`) qui simule un navigateur web pour interagir avec vos vues sans avoir à lancer le serveur de développement.

* **Tester l'index (la page d'accueil) :** Vérifier que si aucun sondage n'existe, un message approprié s'affiche, et que si des sondages passés existent, ils apparaissent bien dans la liste.
* **Tester les détails :** Vérifier qu'un utilisateur qui essaie d'accéder à un sondage futur reçoit bien une erreur `404` (Page introuvable).

### 5. Idées clés à retenir

* **Abondance de biens ne nuit pas :** Écrivez autant de tests que nécessaire (pour le code normal, les cas limites, les erreurs, etc.). Plus vos tests sont précis, plus votre application est sûre.
* **Amélioration continue :** Souvent, lorsqu'un bug est découvert, la meilleure pratique est d'écrire d'abord un test qui échoue à cause de ce bug, puis de modifier le code jusqu'à ce que le test passe.

