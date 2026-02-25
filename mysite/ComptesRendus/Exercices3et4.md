## Exercice 3.2

#### 1. dans le template index.html, ajouter l'affichage de la date de publication du sondage
    
J'ai ajouté:
`- Publié le {{ question.pub_date|date:"d/m/Y" }}`
dans la liste de l'index.html

Le résultat donne:
```text
La terre est-elle plate? - Publié le 21/05/2026
Qui est le président des Etats-Unis? - Publié le 20/03/2026
Quelle langue est parlé en Australie? - Publié le 28/02/2026
Quelle est ta couleur préférée? - Publié le 23/02/2026
Quel projet Théo va-t-il choisir? - Publié le 23/02/2026
```
---

#### 2. ajoutez une page http://127.0.0.1:8000/polls/all/ qui liste tous les sondages avec leur numéro id 
#### et leur titre portant un lien vers leur page de détail

J'ai d'abord ajouté dans `polls/views.py`:
```bash
class AllQuestionsView(generic.ListView):
    template_name = 'polls/all.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.order_by('id')
```
Puis j'ai ajouté la route dans `polls/ulrs.py`:
```bash
path('all/', views.AllQuestionView.as_view(), name='all')
```
Et enfin, j'ai créé un nouveau template `all.html`:
```bash
<h1>Tous les sondages</h1>
<ul>
{% for question in questions %}
    <li>
        #{{ question.id }} —
        <a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a>
    </li>
{% endfor %}
</ul>
```
Le résultat:
```text
Tous les sondages
#1 What's up?
#2 Peut on voyager dans le future?
#3 Quel projet Théo va-t-il choisir?
#4 Quelle langue est parlé en Australie?
#5 Qui est le président des Etats-Unis?
#6 La terre est-elle plate?
#7 Quelle est ta couleur préférée?
```

---
#### Question 3:
Dans cette même page http://127.0.0.1:8000/polls/all/, modifier le lien porté par chaque question pour aboutir 
à une page du type http://127.0.0.1:8000/polls/1/frequency/ affichant les résultats du sondage en valeur absolue 
et en pourcentage plutôt que le formulaire de vote. 
Indice : utiliser la méthode get_choices() de la classe de modèle Question – optionnellement précédemment réalisée –, 
et mettre son résultat dans une variable de gabarit ; s'aider également de Variables pour voir comment accéder 
à un élément d'une variable de gabarit qui est un tuple (ou une liste)

Tout d'abord, j'ai ajouté une nouvelle vue dans `polls/veiws.py`:
```bash
class FrequencyView(generic.DetailView):
    model = Question
    template_name = 'polls/frequency.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['choices'] = self.object.get_choices()
        return context
```
Puis ajout de la route dans `polls/urls.py`:
```bash
path('<int:pk>/frequency/', views.FrequencyView.as_view(), name='frequency')
```
Et l'ajout du template `polls/frequency.html`:
```bash
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in choices %}
    <li>{{ choice.0 }} — {{ choice.1 }} vote(s) ({{ choice.2 }}%)</li>
{% endfor %}
</ul>
```
Résultat (avec question 2): 
```text
Peut on voyager dans le future?
Peut-être - 2 votes (66,67%)
Oui - 1 votes (33,33%)
Non - 0 votes (0,0%)
```
--- 
### Question 4:
4. ajoutez une page de statistiques http://127.0.0.1:8000/polls/statistics/ affichant :
- le nombre total de sondage enregistrés
- le nombre total de choix possibles
- le nombre total de votes – Indice : s'aider de Agrégation > fonction Sum
- la moyenne du nombre de votes par sondage
- [optionnel] la question la plus populaire (ayant reçu le plus de votes) – écrire une méthode de classe pour effectuer ce calcul ainsi que celui qui suit
- [optionnel] la question la moins populaire (ayant reçu le moins de votes)
- la dernière question enregistrée – Indice : s'aider de Agrégation > fonction Max

Note: je ne traite pas les optionnelles dans cette partie!

La première étape, la vue dans `polls/views.py`:
```bash
class StatisticsView(generic.TemplateView):
    template_name = 'polls/statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nb_questions = Question.objects.count()
        nb_choices = Choice.objects.count()
        total_votes = Choice.objects.aggregate(Sum('votes'))['votes__sum'] or 0

        context['nb_questions'] = nb_questions
        context['nb_choices'] = nb_choices
        context['total_votes'] = total_votes
        context['mean'] = round(total_votes / nb_questions, 2) if nb_questions > 0 else 0
        context['last_question'] = Question.objects.order_by('-pub_date').first()
        return context
```
Puis la route dans `polls/urls.py`:
```bash
path('statistics/', views.statistics, name='statistics')
```
Et le template `polls/statistics.html`:
```bash
<h1>Statistiques</h1>
<ul>
    <li>Nombre de sondages : {{ nb_questions }}</li>
    <li>Nombre de choix : {{ nb_choices }}</li>
    <li>Nombre total de votes : {{ total_votes }}</li>
    <li>Moyenne de votes par sondage : {{ moyenne }}</li>
    <li>Dernière question : {{ derniere }}</li>
</ul>
```

Résultat:
```text
Statistiques
Nombre de sondages: 7
Nombre de choix: 20
Nombre total de votes: 9
Moyenne de vote par sondage: 1,29
Derniere question: La terre est-elle plate?
``` 

Questions optionnelles 5 et 6 (plus et moins populaire):

D'abord ajout de méthode dans la class Question dans `polls/models.py`:
```bash
@classmethod
def get_most_popular(cls):
    return cls.objects.annotate(total_votes=Sum('choice__votes')).order_by('-total_votes').first()
@classmethod
def get_least_popular(cls):
    return cls.objects.annotate(total_votes=Sum('choice__votes')).order_by('total_votes').first()
```

Puis, mise a jour de la vue statistics dans `polls/views.py`:
```bash
...
context['most_popular'] = Question.get_most_popular()
context['least_popular'] = Question.get_least_popular()
...
```
Et enfin, la mise a jour du html `templates/polls/statisitics.html`:
```bash
...
<li>Question la plus populaire: {{ most_popular }}</li>
<li>Question la moins populaire: {{ least_popular }}</li>
...
```

Le résultat final:
```text
Statistiques
Nombre de sondages: 7
Nombre de choix: 20
Nombre total de votes: 9
Moyenne de vote par sondage: 1,29
Derniere question: La terre est-elle plate?
Question la plus populaire: Peut on voyager dans le future?
Question la moins populaire: Quel projet Théo va-t-il choisir?
```
---
#### Question 5:
[optionnel] ajoutez un formulaire – accessible par un lien depuis la page http://127.0.0.1:8000/polls/ – 
qui permette de créer une question

Création d'un nouveau fichier `polls/forms.py`:
```bash
from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
        labels = {'question_text': 'Question', 'pub_date': 'Date de publication'}
        widgets = {'pub_date': forms.DateTimeInput(attrs={'type':'datetime-local'}),}
```
Puis ajout de la vue dans `views.py`:
```bash
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.pub_date = timezone.now()
            question.save()
            return redirect('polls:all') 
    else:
        form = QuestionForm()
    return render(request, 'polls/add.html', {'form': form})
```
La route dans `polls/urls.py`:
```bash
path('add/', views.add_question, name= 'add')
```
la création du template `templates/polls/add.html`:
```bash
<h1>Ajouter un sondage</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">créer la question</button>
</form>
<a href="{% url 'polls:all' %}">Retour a la liste</a>
```
Et enfin l'ajout d'un lien vers le formulaire dans `index.hytml`:
```bash
<a href="{% url 'polls:add' %}">+ Ajouter un sondage</a>
```
---

#### Question 6:
[optionnel] enrichissez le pour permettre de saisir les choix possibles de façon simplifiée, 
en prévoyant 5 champs de saisie de choix, seuls les n premiers champs saisis (non vide) 
étant alors pris en compte comme choix de la question

Tout d'abord on ajoute les choix dans la classe QuestionForm dans `polls/forms.py`:
```bash
...
choice_1 = forms.CharField(max_length=200, required=False, label='Choix 1')
choice_2 = forms.CharField(max_length=200, required=False, label='Choix 2')
choice_3 = forms.CharField(max_length=200, required=False, label='Choix 3')
choice_4 = forms.CharField(max_length=200, required=False, label='Choix 4')
choice_5 = forms.CharField(max_length=200, required=False, label='Choix 5')
...
```
Puis on met a jour la vue add_question pour récuperer les choix `polls/views.py`;
```bash
...
choices = [ form.cleaned_data.get(f'choice_{i}') for i in range (1,6)]
for choice_text in choices:
    if choice_text:
        question.choice_set.create(choice_text=choice_text, votes =0)
...
```
---