2.2.1 Exercice d'administration

1. J'ai ajouter admin.site.register(Choice) a polls/admin.py

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

1. for q in Question.objects.all():
    print(q.id, q.question_text, q.pub_date)

2. for q in Question.objects.filter(pub_date__year=2026):
    print(q.question_text, q.pub_date)

3. q = Question.objects.get(pk=2)
 
    print(q.id, q.question_text, q.pub_date)
    for c in q.choice_set.all():
        print(c.choice_text, c.votes)

4. for q in Question.objects.all():
    print(f"Question {q.id}: {q.question_text}")
    for c in q.choice_set.all():
        print(f"  - {c.choice_text}")

5. for q in Question.objects.all():
    print(f"{q.question_text} : {q.choice_set.count()} choix")

7. for q in Question.objects.order_by('-pub_date'):
    print(q.pub_date, q.question_text)


9.  from django.utils import timezone
    q = Question(question_text="Quelle est ta couleur préférée ?", pub_date=timezone.now())
    q.save()
    print(q.id)
