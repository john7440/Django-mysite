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

