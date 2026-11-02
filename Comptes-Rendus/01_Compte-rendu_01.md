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



