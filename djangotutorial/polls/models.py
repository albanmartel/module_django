import datetime

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.db.models import Sum
from django.contrib import admin

MAX_LENGTH = 20


def text_excerpt(text, max_length):
    return text[:max_length] + ('...' if len(text) > max_length else '')


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return "{} {}".format(self.pub_date, text_excerpt(self.question_text, MAX_LENGTH))

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        """
        Returns whether or not the question is published recently.
        la fonction a été corrigée pour que :
        - Seules les questions réellement publiées au cours des dernières 24 heures
         (et dont la date est donc antérieure ou égale à l'instant présent) retournent True.
         - Si une question vient du futur, la seconde condition échoue et la fonction retourne correctement
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def age(self):
        return timezone.now() - self.pub_date

    def get_choices(self):
        resultat = self.choice_set.aggregate(total=Sum('votes'))
        total = resultat['total']
        result_array = []

        if total:
            result_array = [(c.choice_text, c.votes, c.votes / total)
                  for c in self.choice_set.all()]

        return result_array

    def get_max_choice(self):
        resultat = (None, None)

        choices = self.choice_set.all()

        if choices:
            agg_result = self.choice_set.aggregate(total=Sum('votes'))
            total = agg_result['total']

            if not total or total == 0:
                resultat = (choices[0].choice_text, 0)
            else:
                max_choice = max(choices, key=lambda c: c.votes / total)
                resultat = (max_choice.choice_text, max_choice.votes / total)

        return resultat

    def __repr__(self):
        return "<Question: {}>".format(self.question_text)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return text_excerpt(self.choice_text, MAX_LENGTH)


# Le gestionnaire obligatoire pour créer les utilisateurs avec l'email
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'adresse email est obligatoire")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)


# Le modèle utilisateur basé sur AbstractBaseUser (et non AbstractUser)
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)

    # Champs obligatoires pour que l'admin Django et la sécurité fonctionnent
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Configuration de l'authentification par email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Pas de champ supplémentaire requis pour createsuperuser

    objects = CustomUserManager()

    def __str__(self):
        return self.email
