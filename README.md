****# Module Django

Projet python Django de l'Académy Python/JAVA Facylities Multi Services

## Objectif

Apprendre pas à pas l'utilisation de Django à travers les défis de l'académie Python Java

## Gitignore

source du .gitignore <https://djangowaves.com/gitignore-for-a-django-project/>

## Cloner le projet

```bash
git clone https://github.com/albanmartel/module_django.git
```

## Installation de Django

### Pourquoi la version 5.2.18 de Django

La raison est que la dernière version LT (longue terme support). 

C'est une version stable dans le temps qui sera de préférence installé chez un client parce qu'elle est à long terme.

### Installation via l'environnement virtuel 

####  Créer un environnement virtuel Python

À la racine de ton projet :

```bash
python -m venv .venv
```

#### 2. Activation de l'environnement virtuel

Ouvre ton terminal dans le dossier racine de ton projet :

* **Windows (Command Prompt / `cmd.exe`)** :
```cmd
.venv\Scripts\activate.bat
```


* **Windows (PowerShell)** :
```powershell
.venv\Scripts\Activate.ps1
```

*(Si une erreur d'exécution de script apparaît, lance d'abord `Set-ExecutionPolicy Unrestricted -Scope Process` dans ta session).*
* **Linux / macOS** :
```bash
source .venv/bin/activate
```

*`(.venv)` s'affiche au début de la ligne de commande quand l'environnement virtuel est activé.*

Le fichier **.env** doit être enregister à la base du projet

#### 3. Installation de Django

```bash
pip install Django==5.2.18
```

#### 4. Mémoriser les dépendances dans un fichier requirements.txt

```bash
pip freeze > requirements.txt
```

Désormais, le fichier de dépendances 'requirements.txt' permet d'installer les dépendances d'un projet django.

#### 5. Installer Django à partir du fichier de dépendances

il est nécessaire au préalable d'avoir installer l'environnement virtuel et de l'avoir activé.

```bash
python -m pip install -r requirements.txt
```

### Création du squelette de base du site

```cmd
mkdir djangotutorial
django-admin startproject mysite djangotutorial
cd djangotutorial
```

### Création de l'application __Polls__

```cmd
python manage.py startapp polls
```

_La suite du tutorial est ici :_  <https://docs.djangoproject.com/fr/5.2/intro/tutorial01/>


### Démarrage du site de développement 

```python
python manage.py runserver
```