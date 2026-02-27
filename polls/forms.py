from django import forms
from .models import Question

"""
Utilisation de ModelForm pour gerer le formulaire automatiquement,
la classe Meta sert a config le formulaire:
- fields : sont les champs du formulaire
- lasbels : personnalisation du texte
"""
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        labels = {'question_text': 'Question'}
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-control'}),
        }

    choice_1 = forms.CharField(max_length=200, required=False, label='Choix 1',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice_2 = forms.CharField(max_length=200, required=False, label='Choix 2',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice_3 = forms.CharField(max_length=200, required=False, label='Choix 3',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice_4 = forms.CharField(max_length=200, required=False, label='Choix 4',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice_5 = forms.CharField(max_length=200, required=False, label='Choix 5',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))