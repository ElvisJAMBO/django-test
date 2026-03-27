# 📅 Task & Student Management System

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white)

Une application complète de gestion de tâches et d'emplois du temps pour étudiants, développée avec un backend **Django REST Framework** et une application mobile **Flutter**.

## 🚀 Fonctionnalités

- **Authentification Sécurisée :** Connexion via JWT (JSON Web Tokens).
- **Gestion des Tâches (CRUD) :** Création, lecture, mise à jour et suppression de tâches avec images.
- **Gestion des Étudiants :** Profils complets avec photos et emails.
- **Emploi du Temps (Schedule) :** Planification des tâches par étudiant, par jour et par semaine.

## 🛠️ Installation

### 1. Backend (Django)
```bash

# Créer l'environnement virtuel
python -m venv venv
source venv/bin/scripts/activate  # Sur Windows: venv\Scripts\activate

# Installer les dépendances
pip install django djangorestframework django-cors-headers djangorestframework-simplejwt mysqlclient

# Appliquer les migrations
python manage.py migrate

# Lancer le serveur (accessible sur le réseau local)
python manage.py runserver 0.0.0.0:8000