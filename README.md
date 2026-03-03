# Django-mysite - Appli de sondages

Développé avec le Framework Django, c'est le tutoriel officiel avec quelques ajout

## Sommaire

- [Fonctionnalités](#fonctionnalités)
- [Technologies Utilisées](#technologies-utilisées)
- [Structure du projet](#structure-du-projet)
- [Architecture du code](#architecture-du-code)
- [Installation et utilisation](#installation-et-utilisation)
- [Tests](#tests)
  

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
│   └── asgi.py
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
├── requirements.txt                 # Les librairies utilisées
├── manage.py
└── README.md
``` 

## Architecture du code

Le code est structuré selon le pattern MVT (Modèle - Vue - Template) de Django :
1. **models.py** : Définit les modèles Question et Choice avec leurs méthodes métier
2. **views.py**: ensemble de vues Django
3. **forms.py**: basé sur ModelForm avec 5 choix optionnelles
4. **admin.py**: `QuestionAdmin`et `ChoiceAdmin`

## Installation et Utilisation

1. Cloner le projet
```bash
git clone https://github.com/john7440/Django-mysite.git
cd Django-mysite
```

2. Créer et activer un environnement virtuel
```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows/Git Bash
```
3. Installer les dépendances:
```bash
pip install -r requirements.txt
```
4. appliquer les migrations:
```bash
python manage.py migrate
```
5. Créer un super-utilisateur:
```bash
python manage.py createsuperuser
```
7. Lancer le serveur:
```bash
python manage.py runserver
```
7. Acceder à l'application:
- Site: http://127.0.0.1:8000/polls/
- admin: http://127.0.0.1:8000/admin/

## Tests
Les tests automatisés:
```bash
# Lancer tous les tests
python manage.py test polls
```
Les tests vérifient:
- l'affichage correct du formulaire
- la création d'une question sans choix
- la création avec choix
- le rejet d'un formulaire non valide
- l'initialisation des votes à 0
- l'authentification
- l'incrémentation des votes
- plusieurs redirections
- la validité des statistiques

### Licence
Projet réalisé à des fins pédagogiques dans le cadre d'une formation en développement web.
