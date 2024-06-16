# Projet Django Multilang Site

## Table des matières
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Utilisation](#utilisation)
5. [Structure du Projet](#structure-du-projet)
6. [Dépendances](#dépendances)
7. [Contributions](#contributions)
8. [Licence](#licence)

## Introduction

Ce projet est un site web Django multilingue qui permet aux utilisateurs de naviguer entre différentes langues et de consulter des articles de blog. Il intègre également un chatbot basé sur OpenAI pour répondre aux questions des utilisateurs et une fonctionnalité de recherche améliorée.

## Installation

1. Clonez le repository :
```bash
git clone https://github.com/votre_utilisateur/multilang_site.git
cd multilang_site
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Configuration
### Pour configurer la base de donnée, qui permets de gérer les articles il vous faut exécuter ces commandes :
```bash
python manage.py makemigrations
python manage.py migrate
```
### Pour pouvoir utiliser la "Messagerie d'aide" (ou Chatbot en anglais), vous devez posséder une clé d'API OPENAI.
Il est modifiable dans le fichier multilang_site/main/views.py, en remplaçant 'test' par votre clé d'API :
```py
client = OpenAI(
    ## Tested with a real api key, but for lack of resources here's a placeholder ##
    api_key='test',
)
```
Assurez-vous que vous ayez ajouté des coins dans votre clé d'API sinon cela ne marchera pas.


## Utilisation
- Pour lancer le serveur de développement Django :

```py
python manage.py runserver
```

- Accédez au site dans votre navigateur à l'adresse http://127.0.0.1:8000 (peut changer selon vos paramètres)

### Pour ajouter des articles sur le site :
- Exécutez cette commande pour créer un utilisateur pour la base de donnée, et suivez les instructions.
```py
py manage.py createsuperuser
```    
- Accedez à http://127.0.0.1:8000/admin en vous connectant.
- Vous accèderez à une interface qui vous permettra d'ajouter des articles en allant sur la catégorie "main", puis appuyer sur le bouton "+" dans "Articles".

## Structure du Projet
La structure du projet est la suivante :

```arduino
multilang_site/
├── main/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   └── ...
├── multilang_site/
│   ├── settings.py
│   ├── urls.py
│   ├── ...
├── manage.py
├── requirements.txt
└── README.md
```

## Dépendances
Les principales dépendances de ce projet sont listées dans le fichier requirements.txt.