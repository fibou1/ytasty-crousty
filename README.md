# ytasty-crousty
Projet fullstack de bout en bout : commande client, gestion opérationnelle restaurant et pilotage direction. Python/FastAPI, React/TypeScript, PostgreSQL, Docker. Réalisé en autonomie dans le cadre d'une montée en compétences infra/dev.

* **Jour 1** :
  * 📐 Conception du Modèle Conceptuel de Données (MCD) avec Looping.
  * 📁 Création de l'arborescence complète du projet.

* **Jour 2** :
  * 🐳 **Conteneurisation globale** : Configuration de l'environnement de développement multi-conteneurs avec Docker Compose.
  * ⚙️ **Gestion des environnements** : Sécurisation de l'infrastructure via un fichier `.env` (exclu de Git) pour isoler les identifiants de la base de données.
  * 🗄️ **Base de données** : Déploiement d'un conteneur PostgreSQL avec persistance des données via un volume Docker et configuration d'un script de vérification de santé (*healthcheck*) robuste.
  * 🚀 **API Backend** : Dockerisation de l'application FastAPI (Python 3.12-slim) avec rechargement automatique au développement et résolution des conflits de ports réseaux.