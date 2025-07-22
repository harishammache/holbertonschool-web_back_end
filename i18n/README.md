<h1 align="center">🌍 Flask i18n - Internationalisation avec Flask-Babel</h1>

<div align="center">
    <img src="./img/i18n.png" alt="Flask i18n Project" width="200">
</div>

---

## 📖 Introduction

L'internationalisation (**i18n**) est une étape cruciale dans le développement d'applications web accessibles à une audience globale.  
Ce projet t’apprend à construire une application Flask capable de s’adapter dynamiquement à la langue et au fuseau horaire de l’utilisateur.  

Tu vas apprendre à :  
- Paramétrer **Flask-Babel** pour gérer plusieurs langues  
- Détecter automatiquement la **locale** via l’URL, la session utilisateur ou les headers HTTP  
- Localiser dynamiquement les **horodatages** avec `pytz`  

---

## 🧠 Concepts clés

### 🌐 Internationalisation (i18n)
- Permet à une application de **supporter plusieurs langues** sans changer son code métier  
- On prépare des messages **traductibles** via des fichiers `.po` et `.mo`

### 🧭 Localisation (l10n)
- Affiche des **textes traduits**, adaptés à la culture ou région de l’utilisateur  
- Gère les **dates, heures, formats de nombres** selon les préférences régionales

### 🕓 Localisation des timestamps
- Grâce à `pytz`, tu peux convertir les dates en **heure locale utilisateur**  
- Idéal pour les applications affichant des événements, publications, historiques, etc.

---

## 🧰 Technologies & Librairies

- `Flask` : micro-framework web Python  
- `Flask-Babel` : extension i18n pour Flask  
- `pytz` : gestion des fuseaux horaires  
- `gettext` : moteur de traduction  

---

## 🧪 Structure du projet

```bash
.
├── app.py                 # Application Flask principale
├── babel.cfg             # Configuration des extractions de messages
├── translations/         # Répertoire des fichiers de traduction
│   └── fr/               # Ex. : Traduction française
│       └── LC_MESSAGES/
│           ├── messages.po
│           └── messages.mo
├── templates/
│   └── index.html        # Template paramétrable avec Flask-Babel
├── static/
│   └── ...
└── README.md

```

## 🧼 Bonnes pratiques

✅ Respecter la structure du projet et nommer correctement les fichiers  
✅ Toujours documenter modules, classes et fonctions  
✅ Utiliser les **annotations de types** (`-> str`, `-> None`, etc.)  
✅ Rendre tous les fichiers `.py` **exécutables**  
✅ Vérifier la **conformité PEP8** avec `pycodestyle` (v2.5) 

## 🧑‍💻 Auteur

Hammache Haris  
🔗 [GitHub - harishammache](https://github.com/harishammache)

---