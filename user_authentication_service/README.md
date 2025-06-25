<h1 align="center">🔐 Session Authentication Project</h1>

<div align="center">
    <img src="./img/session.png" alt="Session Authentication Project" width="200">
</div>

<p align="center">
    <strong>Implémentation d'un système d'authentification par session avec Flask</strong><br>
    <em>Un projet pédagogique pour comprendre le mécanisme des sessions côté backend</em>
</p>

---

## 📚 Description

Ce projet met en œuvre une **authentification par session** pour une API REST développée avec Flask.  
Tu y apprendras à manipuler les **Cookies HTTP**, à créer et gérer une session utilisateur, le tout **sans utiliser de module externe**, dans un but purement pédagogique.

Il comprend :

- 🍪 L'envoi et la lecture de **cookies HTTP**
- 🆔 La création d'un identifiant de session unique
- 🧠 Le lien entre une session et un utilisateur
- 🔓 Le mécanisme de connexion et de déconnexion via des endpoints Flask
- 🧹 La gestion de la session (création, récupération, destruction)

---

## 🧠 Objectifs pédagogiques

- Comprendre ce qu'est une **authentification**
- Différencier **authentification** et **autorisation**  
- Comprendre les **Cookies** : rôle, envoi et lecture
- Implémenter un mécanisme d'authentification basé sur les **sessions**
- Créer, stocker, retrouver et supprimer une session utilisateur
- Comprendre les limitations de ce système et pourquoi on utilise des bibliothèques dédiées en production

---

## ⚙️ Technologies utilisées

- Python 3.9 (Ubuntu 20.04)
- Flask
- Cookies HTTP
- UUID
- Dictionnaires Python (pour stocker les sessions)
- Sans aucune dépendance externe

---

## ⚙️ Setup & Installation

### Prerequisites
```bash
# Install required dependencies
pip3 install flask
```

### Running the Project
```bash
# Set environment variables
export API_HOST=0.0.0.0
export API_PORT=5000
export AUTH_TYPE=session_auth
export SESSION_NAME=_my_session_id

# Run the Flask application
python3 -m api.v1.app
```

---

## ✅ Requis du projet

- Tous les fichiers sont exécutables (`chmod +x`)
- Une ligne vide à la fin de chaque fichier
- Conformité PEP8 (`pycodestyle` 2.5)
- Documentation obligatoire :
  - Chaque module
  - Chaque classe
  - Chaque méthode/fonction (avec explication claire de son rôle)
- Aucune dépendance externe autorisée
- Utilisation des modules standards uniquement

---

## 🚀 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth_session/login` | Connexion utilisateur |
| DELETE | `/api/v1/auth_session/logout` | Déconnexion utilisateur |
| GET | `/api/v1/users/me` | Profil utilisateur courant |

---

## 📝 Author

**Haris** – Développeur Web Full-Stack  
GitHub: [@harishammache](https://github.com/harishammache)
