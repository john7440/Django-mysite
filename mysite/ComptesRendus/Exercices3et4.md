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
def all_questions(request):
    questions = Question.objects.order_by('id')
    return render(request, 'polls/all.html', {'questions': questions})
```
Puis j'ai ajouté la route dans `polls/ulrs.py`:
```bash
path('all/', views.all_questions, name='all')
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
def frequency(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.get_choices()
    return render(request, 'polls/frequency.html', {
        'question': question,
        'choices': choices
    })
```
Puis ajout de la route dans `polls/urls.py`:
```bash
path('<int:question_id>/frequency/', views.frequency, name='frequency')
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

