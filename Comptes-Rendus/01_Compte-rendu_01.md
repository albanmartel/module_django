# Premier Compte rendu

__Suivi de la documentation officielle:__ <https://docs.djangoproject.com/fr/5.2/intro/tutorial01/>

## Création du répertoire du projet

```bash
mkdir djangotutorial
```

##  Initier un nouveau projet Django :

```bash
django-admin startproject mysite djangotutorial
```

## Voir ce qui a été créé

```cmd
ls .\djangotutorial\


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        02/11/2026     13:31                mysite
-a----        02/11/2026     13:31            684 manage.py
```

### Se rendre dans le projet créé Django

```cmd
cd djangotutorial
```

### Lancer le serveur Django
```cmd
python manage.py runserver
```

### traces d'exécution

```cmd
 python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
November 02, 2026 - 13:39:32
Django version 5.2.18, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
[02/Nov/2026 13:40:18] "GET / HTTP/1.1" 200 12068
```

### Création de l'application *polls*

```cmd
python manage.py startapp polls
```

### Voir les modifications du répertoire

```cmd
ls


    Répertoire: djangotutorial


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        02/11/2026     13:39                mysite
d-----        02/11/2026     13:45                polls
-a----        02/11/2026     13:39              0 db.sqlite3
-a----        02/11/2026     13:31            684 manage.py

```

### La vue avant modification

```cmd
 cat .\views.py
from django.shortcuts import render

# Create your views here.
```

### La vue après modification

```cmd
 cat .\views.py
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

### Rooter l'url pour que la requête parvienne à la bonne vue

#### Le fichier _polls/urls.py_

Par défaut ce fichier n'existe pas

_sous git bash_
```bash
vim urls
```

appuyer sur i 

coller le contenu du tutoriel : 
```
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

Pour enregistrer : tapper :wq! 

```
:wq!
```

Vérifier le contenu 

```bash
_django/djangotutorial/polls (main)
$ cat urls
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

### Configurer l'url racine du site

L'url racine ce situe sous _mysite/urls.py_

#### Avant modification

```bash
$ cat mysite/urls.py
"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

effacer le contenu et remplacer par ceci : 

```bash
**from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]**
```

## Ecriture de votre première application Django partie 2


### Changement des variables existantes : 

_LANGUAGE_CODE_ et _TIME_ZONE_

1. Valeurs d'origine

```bash
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
```

2. Valeurs après  modification

```bash
LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Paris'
```

### Accès à la BDD

Par défaut ma base de données locale est vide , même si elle existe.

Pour mettre ma base de données au niveau de ce qui est attendu par django, j'exécute la commande suivante :

```bash
python manage.py migrate
```

En me rendant dans l'outil dbbrowser, je me rends bien compte que suite à sa base s'est en partie peuplée.

### Accéder au shell de django

la commande permet d'accéder au shell de Django:

```bash
python manage.py shell
```

```bash
djangotutorial> python manage.py shell
6 objects imported automatically (use -v 2 for details).

Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
```

### Création de 2 modèles : _Question et Choice_

### 1.  Avant modification contenu du fichier _polls/models.py_

```bash
djangotutorial (main)
$ cat polls/models.py
from django.db import models

# Create your models here.
```

### 2. Après modification contenu du fichier _polls/models.py_

```bash
djangotutorial (main)
$ cat polls/models.py
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

### Activation des modèles


#### Avant modification

```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

#### Après modification

```bash
INSTALLED_APPS = [
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### Actualiser les changements dans la base de données

```bash
python manage.py makemigrations polls
```

Cette commande ne créé pas la table polls dans la base de données

par contre la suivante permet de la faire

```bash
python manage.py sqlmigrate polls 0001
```

### Créer un utilisateur privilégié

```bash
djangotutorial> python manage.py createsuperuser
Username (leave blank to use 'martela'): alban
Email address: alban.f.j.martel@laposte.net
Password:
Password (again):
Error: Your passwords didn't match.
Password:
Password (again):
Superuser created successfully.
(.venv) PS djangotutorial>
```
