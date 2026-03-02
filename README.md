# Django-mysite - Appli de sondages

Développé avec le Framework Django, c'est le tutoriel officiel avec quelques ajout

## Sommaire

- [Fonctionnalités](#fonctionnalités)
- [Technologies Utilisées](#technologies-utilisées)
- [Structure du projet](#structure-du-projet)
  

## Fonctionnalités

#### Partie Utilisateur:
- **Liste de sondages**: la liste des sondages récents avec la date de publication
- **Vote**: Formulaire de vote avec choix radio
- **Résultats**: Affichage des résultats après vote avec le nombre de votes
- **Frequences**: Visualisation des résultats en pourcentage
- **Tous les sondages**: Tous les sondages
- **Statistiques**: Statistiques globales (choix, votes, moyenne,...)

#### Partie Administration:
- **Interface admin Django**: Gestion CRUD des sondages
- **Création de sondage**: formulaire d'ajout d'un sondages avec jusqu'a 5 choix
- **Gestion des utilisateurs**: création, activation/desactivation de compte
- **Authentification**: Connexion/deconnexion + restriction pour la création de sondage
 
## Technologies Utilisées

- **Python 3.14** & **Django 5.2**
- **Bootstrap 5** : Interface responsive avec composants (cards, navbar, badges)
- **CSS personnalisé** : fichier `style.css` pour personnalisation
- **SQLite** : base de données par défaut fournie par Django

## Structure du projet

```text
DjangoTest/
├── mysite/
│   └── ComptesRendus                # Compte rendu des exercices
|   |   ├── Exercice1et2.md
│   │   └── Exercice3et4.md
│   ├── settings.py                  # Configuration du projet
│   ├── urls.py                      # Routes principales
│   ├── wsgi.py
│   ├── asgi.py
│   └── requirements.txt             # Les librairies utilisées
├── polls/
│   ├── static/
│   │   └── polls/
│   │       ├── css/
│   │       │   └── style.css        # CSS personnalisé
│   │       └── images/              # Images du site
│   ├── templates/
│   │   └── polls/
│   │       ├── index.html           # Page d'accueil
│   │       ├── detail.html          # Page de vote
│   │       ├── results.html         # Page de résultats
│   │       ├── all.html             # Tous les sondages
│   │       ├── frequency.html       # Fréquences et pourcentages
│   │       ├── statistics.html      # Tableau de bord statistiques
│   │       └── add.html             # Formulaire d'ajout
│   ├── admin.py                     # Configuration de l'interface admin
│   ├── forms.py                     # Formulaire de création de sondage
│   ├── models.py                    # Modèles Question et Choice
│   ├── tests.py                     # Tests 
│   ├── urls.py                      # Routes de l'application
│   └── views.py                     # Vues
├── templates/
│   ├── base.html                    # Gabarit parent
│   └── registration/
│       └── login.html               # Page de connexion
├── manage.py
└── README.md
``` 
