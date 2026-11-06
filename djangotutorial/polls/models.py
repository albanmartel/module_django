import datetime

from django.db import models
from django.utils import timezone
from django.db.models import Sum

MAX_LENGTH = 20


def text_excerpt(text, max_length):
    return text[:max_length] + ('...' if len(text) > max_length else '')


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return "{} {}".format(self.pub_date, text_excerpt(self.question_text, MAX_LENGTH))
    
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
        return [(c.choice_text, c.votes, c.votes / total)
                for c in self.choice_set.all()]

    def get_max_choice(self):
        choices = self.choice_set.all()
        resultat = self.choice_set.aggregate(total=Sum('votes'))
        total = resultat['total']
        max_choice = max(choices, key=lambda c: c.votes / total)
        return max_choice.choice_text, max_choice.votes / total if total > 0 else None

    def __repr__(self):
        return "<Question: {}>".format(self.question_text)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return text_excerpt(self.choice_text, MAX_LENGTH)
