#!/bin/bash


# Appliquer les migrations
python manage.py migrate

# Démarrer le serveur
python manage.py runserver 0.0.0.0:8000