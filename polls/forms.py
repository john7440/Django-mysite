from django import forms
from .models import Question

"""
Utilisation de ModelForm pour gerer le formulaire automatiquement,
la classe Meta sert a config le formulaire:
- fields : sont les champs du formulaire
- lasbels : personnalisation du texte
- widget: afficher un calendrier
"""
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
        labels = {'question_text': 'Question', 'pub_date': 'Date de publication'}
        widgets = {'pub_date': forms.DateTimeInput(attrs={'type':'datetime-local'}),}