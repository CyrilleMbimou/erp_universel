# Installation et configuration de l’ERP Universel

## 1. Installation et configuration

- Installe les dépendances Python :
  ```sh
  pip install -r requirements.txt
  ```
- Installe les dépendances Node.js pour Tailwind :
  ```sh
  npm install
  ```
- Compile le CSS Tailwind :
  ```sh
  npm run build:css
  ```
- Lance les conteneurs Docker :
  ```sh
  docker-compose up
  ```
- Effectue les migrations Django dans le conteneur :
  ```sh
  docker-compose exec web python manage.py makemigrations
  docker-compose exec web python manage.py migrate
  ```

## 2. Tests de base

- Accède à l’admin Django : http://localhost:8000/admin/
- Ajoute quelques données de test via l’admin.

## 3. Navigation et ergonomie

- Un menu global est présent sur toutes les pages (voir `core/templates/base.html`).
- L’interface utilise Tailwind CSS pour un design moderne et responsive.

## 4. Fonctionnalités CRUD

- Ajoute des formulaires pour créer, modifier, supprimer des objets (voir la doc Django).
- Utilise les vues génériques Django ou HTMX pour plus de dynamisme.

## 5. Rapports et tableaux de bord

- Ajoute des indicateurs sur le dashboard (nombre de clients, ventes du mois, alertes stock…).
- Prépare des exports PDF/Excel si besoin.

## 6. Sécurité et déploiement

- (Optionnel) Ajoute l’authentification si besoin.
- Prépare le déploiement (paramètres de production, sauvegardes, etc.).

## 7. Documentation et tests

- Documente chaque module et chaque modèle.
- Ajoute des tests unitaires pour sécuriser l’évolution du projet.
