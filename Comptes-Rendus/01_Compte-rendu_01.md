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
