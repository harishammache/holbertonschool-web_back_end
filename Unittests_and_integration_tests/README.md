<h1 align="center">🧪 Unit Testing & Integration Testing Project</h1>

<div align="center">
    <img src="./img/unittest.png" alt="Unit Testing Project" width="200">
</div>

---

## 📖 Introduction

Les tests unitaires et les tests d’intégration sont des piliers essentiels pour garantir la fiabilité et la robustesse de ton code.  

Ce projet te permet de comprendre et maîtriser :  
- La différence entre **tests unitaires** et **tests d’intégration**  
- Les bonnes pratiques pour écrire des tests efficaces en Python avec le module natif `unittest`  
- L’utilisation du **mocking** pour isoler la logique métier  
- L’organisation des tests dans un projet réel  

---

## 🧠 Concepts clés

### Tests Unitaires  
- Testent une fonction ou méthode spécifique, isolée de ses dépendances  
- Vérifient que la logique interne produit bien les résultats attendus sur plusieurs cas  
- Les appels externes sont **mockés** pour ne tester que la fonction ciblée  

### Tests d’Intégration  
- Testent des scénarios complets impliquant plusieurs composants  
- Valident la communication et interaction entre les modules  
- Peuvent mocker uniquement les appels réseau, fichiers, bases de données, etc.  

---

## 🚀 Exécuter les tests

Lance un fichier de tests avec :  
```bash
python3 -m unittest path/to/test_file.py
```

## 📝 Author

Hammache Haris: [harishammache](https://github.com/harishammache)