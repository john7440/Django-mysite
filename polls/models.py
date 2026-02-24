import datetime

from django.utils import timezone
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    #ajout de [:20] pour les 20 premiers caractères
    def __str__(self):
        return self.question_text[:20]

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    #Qurestion 1 (2.2.3) -age de la question
    def age(self):
        return timezone.now() - self.pub_date

    #Question 3 -afficher la date de la publication
    def age_with_date(self):
        return f"{self.question_text[:20]}: publié le {self.pub_date.strftime('%d/%m/%Y')}"

    #Question4 -methode get_choices
    def get_choices(self):
        choices = self.choice_set.all()
        total_votes = sum(c.votes for c in choices)
        result = []
        for c in choices:
            proportion = (c.votes / total_votes * 100) if total_votes > 0 else 0
            result.append((c.choice_text,c.votes, round(proportion,2)))
        return result

    #Q5
    def get_max_choice(self):
        choices = self.choice_set.all()
        total_votes = sum(c.votes for c in choices)
        best = max(choices, key=lambda c: c.votes)
        proportion = (best.votes / total_votes * 100) if total_votes > 0 else 0
        return (best.choice_text, best.votes, round(proportion, 2))


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text[:20]