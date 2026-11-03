# Compte-Rendu exercice 2.2.1

## 1. Etape 1

Visualisation interface faite.
Implémentation de l'interface Choice dans Admin faite.

## 2. Etape 2

Création terminée de 5 questions avec leur choix 

## 3. Etape 3

### 3.1. Voyez-vous les attributs de vos classes ?

Oui les attributs des classes sont visibles depuis l'interface Admin

### 3.2 Pouvez-vous filtrer vos données suivants tous les attributs ?

Non

### 3.3 Pouvez-vous trier vos données suivants tous les attributs ?

Non

### 3.4 Pouvez-vous chercher un contenu parmi tous les champs ?

Non

## 4. Ajout de fonctionnalités à l'interface d'administration.

Le code suivant permet d'afficher en triant par date de la plus récente à la plus ancienne. Filtrer les résultats et recherché par du contenu de champs ont été ajoutés.

```Python
class QuestionAdmin(admin.ModelAdmin):
    date_hierarchy = "pub_date"
    # Trier de la plus récente à la plus anvienne
    ordering = ["-pub_date"]
    # Afficher les champs suivants de la liste
    list_display = ("question_text", "pub_date", "id")
    # Filtrer La liste des questions par les critères texte de la question, date de la question puis sont id
    list_filter = ("question_text", "pub_date", "id")
    # Chercher par champs
    search_fields = ("question_text", "pub_date", "id")
```

### 5. Ajoutez un nouvel utilisateur via l'interface d'admin. 

Il n'est pas possible de se connecter avec ce nouveau compte.

### 6. Donner à l'utilisateur le droit de se connecter à l'interface d'admin

Je coche la case Staff status pour donner à l'utilisateur "vincent" l'autorisation d'accéder à l'interface admin.
Je donne à "vincent" les autorisations suivantes : 
```txt
Polls | Choice | Can view choice
Polls | Question | Can view question
Sessions | session | Can view session
```

L'utilisateur "vincent" peut se connecter mais il a des droits restreints.

### 7. Déactiver l'utilisateur 

Je décoche le compte vincent pour voir s'il est toujours actif.

Après déconnection et reconnexion il est devenu impossible à "Vincent" de ce connecter. 


