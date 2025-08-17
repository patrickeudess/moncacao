# 🌱 Mon Cacao - Application d'Analyse et Prédiction de Productivité

Une application web complète pour l'analyse et la prédiction de la productivité du cacao, intégrant des fonctionnalités d'IA, d'analyse de données et de score écologique.

## 🚀 Fonctionnalités Principales

### 📊 Tableau de Bord Interactif
- Visualisations en temps réel de la production
- Graphiques de tendances et analyses
- Métriques de performance clés

### 🤖 Prédictions IA
- Modèle XGBoost pour prédire la productivité
- Interface intuitive pour saisir les paramètres
- Résultats détaillés avec explications

### 🌿 Score Écologique
- Évaluation de l'impact environnemental
- Indicateurs de durabilité
- Recommandations d'amélioration

### 📈 Analyse des Revenus
- Suivi des revenus par période
- Projections financières
- Analyse de rentabilité

### 💡 Assistant IA
- Conseils personnalisés
- Recommandations d'optimisation
- Support multilingue

## 🛠️ Technologies Utilisées

- **Backend**: Python, Flask, XGBoost
- **Frontend**: HTML5, CSS3, JavaScript
- **Base de données**: SQLite
- **IA/ML**: Scikit-learn, Pandas, NumPy
- **Visualisation**: Chart.js, Plotly

## 📋 Prérequis

- Python 3.8+
- pip (gestionnaire de paquets Python)

## 🔧 Installation

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/votre-username/mon-cacao.git
   cd mon-cacao
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Lancer l'application**
   ```bash
   python api_server.py
   ```

4. **Ouvrir dans le navigateur**
   ```
   http://localhost:5000
   ```

## 📁 Structure du Projet

```
mon-cacao/
├── api_server.py              # Serveur Flask principal
├── cacao1.py                  # Logique métier principale
├── model_productivite_xgb.pkl # Modèle XGBoost entraîné
├── requirements.txt           # Dépendances Python
├── frontend/                  # Interface utilisateur
│   ├── index.html            # Page d'accueil
│   ├── dashboard.html        # Tableau de bord
│   ├── prediction.html       # Prédictions IA
│   ├── score-ecologique.html # Score écologique
│   ├── css/                  # Styles CSS
│   └── js/                   # Scripts JavaScript
└── docs/                     # Documentation
```

## 🎯 Utilisation

### 1. Accès à l'Application
- Ouvrez `http://localhost:5000` dans votre navigateur
- Naviguez entre les différentes sections via le menu

### 2. Prédictions de Productivité
- Rendez-vous sur la page "Prédictions"
- Saisissez les paramètres de votre plantation
- Obtenez une prédiction de productivité

### 3. Analyse du Score Écologique
- Accédez à la section "Score Écologique"
- Évaluez l'impact environnemental
- Consultez les recommandations

### 4. Tableau de Bord
- Visualisez les métriques clés
- Analysez les tendances
- Suivez les performances

## 🔍 Fonctionnalités Avancées

### Modèle XGBoost
- Prédiction précise basée sur l'historique
- Variables d'entrée optimisées
- Validation croisée intégrée

### Interface Responsive
- Design adaptatif pour mobile et desktop
- Navigation intuitive
- Chargement optimisé

### Analyse en Temps Réel
- Mise à jour automatique des données
- Graphiques interactifs
- Export des résultats

## 📊 Métriques et Indicateurs

- **Productivité**: kg/ha par saison
- **Score Écologique**: 0-100 (durabilité)
- **Revenus**: Projections financières
- **Tendances**: Évolution temporelle

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Fork le projet
2. Créez une branche pour votre fonctionnalité
3. Committez vos changements
4. Poussez vers la branche
5. Ouvrez une Pull Request

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 📞 Support

Pour toute question ou problème :
- Ouvrez une issue sur GitHub
- Consultez la documentation dans le dossier `docs/`

## 🔄 Mises à Jour

### Version 1.0
- ✅ Interface utilisateur complète
- ✅ Modèle de prédiction XGBoost
- ✅ Score écologique intégré
- ✅ Tableau de bord interactif
- ✅ Assistant IA
- ✅ Analyse des revenus

---

**Développé avec ❤️ pour l'agriculture durable du cacao**
