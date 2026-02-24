2.2.1 Exercice d'administration

1. J'ai ajouté admin.site.register(Choice) a polls/admin.py

2. Fait

3. Voyez-vous tous les attributs de vos classes ? Oui si on clique
   Pouvez-vous filtrer vos données suivants tous les attributs ? Non
   Pouvez-vous trier vos données suivants tous les attributs ? Non 
   Pouvez-vous chercher un contenu parmi tous les champs ? Non

4.1
 .2
 .3 Implémentation dans polls/admin.py   

5.Non
6. Fait en cochant le statut d'équipe
7. Décocher actif

----------------------------------------------------------
2.2.2 Exercice shell

1. Lister tous les objets de type Question : faites une boucle pour afficher les 
attributs de chaque question sur une ligne différente. Indice : remarquer que Question.objects.all()
est un itérable sur lequel vous pouvez boucler avec une simple boucle for
- Query:
```bash
 for q in Question.objects.all():
    print(q.id, q.question_text, q.pub_date)
```
- Résultat:
```text
1 What's up? 2026-02-23 12:19:04+00:00
2 Peut on voyager dans le future? 2026-02-10 12:19:04+00:00
3 Quel projet Théo va-t-il choisir? 2026-02-23 14:00:00+00:00
4 Quelle langue est parlé en Australie? 2026-02-28 12:33:14+00:00
5 Qui est le président des Etats-Unis? 2026-03-20 14:00:00+00:00
6 La terre est-elle plate? 2026-05-21 16:00:00+00:00
```

---

2. Ajoutez un filtre sur la date de publication – portant par ex. sur un de ses composants 4 suivants : 
year, month, day – de vos questions et lister un sous-ensemble de vos questions suivant 
les dates que vous avez saisies à l'exercice précédent.
```bash
for q in Question.objects.filter(pub_date__year=2026):
    print(q.question_text, q.pub_date)
```

```text
What's up? 2026-02-23 12:19:04+00:00
Peut on voyager dans le future? 2026-02-10 12:19:04+00:00
Quel projet Théo va-t-il choisir? 2026-02-23 14:00:00+00:00
Quelle langue est parlé en Australie? 2026-02-28 12:33:14+00:00
Qui est le président des Etats-Unis? 2026-03-20 14:0
```
---
3. Trouvez la deuxième question (pour laquelle l'attribut de clé primaire id = 2) 
de votre base de données, puis affichez les valeurs de tous ses attributs et tous les choix associés.

```bash
q = Question.objects.get(pk=2)
print(q.id, q.question_text, q.pub_date)
for c in q.choice_set.all():
   print(c.choice_text, c.votes)
```
```text
Oui 0
Non 0
Peut-être 0
```

---

4. Faites une boucle pour afficher les attributs de chaque question et leurs choix associés.
```bash
for q in Question.objects.all():
    print(f"Question {q.id}: {q.question_text}")
for c in q.choice_set.all():
    print(f"  - {c.choice_text}")
```

```text
Question 1: What's up?
 - Not much
 - The sky
Question 2: Peut on voyager dans le future?
 - Oui
 - Non
 - Peut-être
Question 3: Quel projet Théo va-t-il choisir?
 - Le quizz
 - Quizz
 - Un quizz
Question 4: Quelle langue est parlé en Australie?
 - Australien
 - Australopitheque
 - Anglais
Question 5: Qui est le président des Etats-Unis?
 - DaSilva Rafael
 - Donald Trump
 - Mickey Mouse
Question 6: La terre est-elle plate?
 - Non
 - Peut-être
 - De tout évidence
```

---
5.Affichez le nombre de choix enregistrés pour chaque question

```bash
for q in Question.objects.all():
    print(f"{q.question_text} : {q.choice_set.count()} choix")
```
```text
What's up? : 2 choix
Peut on voyager dans le future? : 3 choix
Quel projet Théo va-t-il choisir? : 3 choix
Quelle langue est parlé en Australie? : 3 choix
Qui est le président des Etats-Unis? :3 choix
```

---

7. Triez les questions par ordre antéchronologique

```bash
for q in Question.objects.order_by('-pub_date'):
    print(q.pub_date, q.question_text)
```
```text
2026-05-21 16:00:00+00:00 La terre est-elle plate?
2026-03-20 14:00:00+00:00 Qui est le président des Etats-Unis?
2026-02-28 12:33:14+00:00 Quelle langue est parlé en Australie?
2026-02-23 14:00:00+00:00 Quel projet Théo va-t-il choisir?
2026-02-23 12:19:04+00:00 What's up?
2025-08-20 11:19:04+00:00 Peut on voyager dans le future?
```
---
9. Créez une question en utilisant le shell

```bash
from django.utils import timezone
q = Question(question_text="Quelle est ta couleur préférée ?", pub_date=timezone.now())
q.save()
print(q.id)
```
```text
7
```
---
10. Ajoutez 3 choix à cette question en utilisant le shell
```bash
q.choice_set.create(choice_text="Rouge", votes=0)
q.choice_set.create(choice_text="Bleu", votes=0)
q.choice_set.create(choice_text="Vert", votes=0)
```
---

11. 
```bash
import datetime
from django.utils import timezone
recentes = Question.objects.filter(pub_date__gte=timezone.now() - datetime.timedelta(days=30))
for q in recentes:
    print(q.question_text, q.pub_date)
```

```text
What's up? 2026-02-23 12:19:04+00:00
Quel projet Théo va-t-il choisir? 2026-02-23 14:00:00+00:00
Quelle langue est parlé en Australie? 2026-02-28 12:33:14+00:00
Qui est le président des Etats-Unis? 2026-03-20 14:00:00+00:00
La terre est-elle plate? 2026-05-21 16:00:00+00:00
Quelle est ta couleure préférée? 2026-02-23 14:06:38.249899+00:00
```

---
12.
```bash
from django.contrib.auth.models import User
for u in User.objects.all():
    print(u.id, u.username, u.email, u.is_staff)
```
```text
1 admin admin@example.com True
2 test user@example.com True
```