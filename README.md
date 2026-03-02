# Django-mysite - Appli de sondages

Développé avec le Framework Django, c'est le tutoriel officiel avec quelques ajout

## Sommaire

- [Fonctionnalités](#fonctionnalités)
- [Technologies Utilisées](#technologies-utilisées)
  

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
