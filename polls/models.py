import datetime

from django.utils import timezone
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    #ajout de (:20]  pour les 20 premiers caractères
    def __str__(self):
        return self.question_text[:20]

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    #Qurestion 1 (2.2.3) -age de la question
    def age(self):
        return timezone.now() - self.pub_date

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text[:20]