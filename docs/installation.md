# 🔧 Guide d'Installation - Mon Cacao

## 📋 Prérequis

### Système d'Exploitation
- **Windows** 10/11
- **macOS** 10.14 ou supérieur
- **Linux** (Ubuntu 18.04+, CentOS 7+)

### Logiciels Requis
- **Python** 3.8 ou supérieur
- **pip** (gestionnaire de paquets Python)
- **Git** (pour cloner le repository)

## 🚀 Installation Étape par Étape

### 1. Vérification de Python

```bash
# Vérifier la version de Python
python --version
# ou
python3 --version
```

**Résultat attendu** : `Python 3.8.x` ou supérieur

### 2. Clonage du Repository

```bash
# Cloner le projet
git clone https://github.com/votre-username/mon-cacao.git

# Accéder au répertoire
cd mon-cacao
```

### 3. Création d'un Environnement Virtuel (Recommandé)

#### Windows
```bash
# Créer l'environnement virtuel
python -m venv .venv

# Activer l'environnement
.venv\Scripts\activate
```

#### macOS/Linux
```bash
# Créer l'environnement virtuel
python3 -m venv .venv

# Activer l'environnement
source .venv/bin/activate
```

### 4. Installation des Dépendances

```bash
# Mettre à jour pip
pip install --upgrade pip

# Installer les dépendances
pip install -r requirements.txt
```

### 5. Vérification de l'Installation

```bash
# Vérifier que Streamlit est installé
streamlit --version

# Vérifier que le modèle existe
ls model_productivite_xgb.pkl
```

## 🎯 Lancement de l'Application

### Méthode Simple
```bash
streamlit run cacao1.py
```

### Méthode avec Options
```bash
# Spécifier le port
streamlit run cacao1.py --server.port 8501

# Spécifier l'adresse
streamlit run cacao1.py --server.address localhost

# Mode développement
streamlit run cacao1.py --server.runOnSave true
```

### Accès à l'Application
1. **Ouvrir votre navigateur**
2. **Aller à** : `http://localhost:8501`
3. **L'application devrait s'ouvrir automatiquement**

## 🔧 Configuration Avancée

### Variables d'Environnement

#### Windows
```cmd
set STREAMLIT_SERVER_PORT=8501
set STREAMLIT_SERVER_ADDRESS=localhost
```

#### macOS/Linux
```bash
export STREAMLIT_SERVER_PORT=8501
export STREAMLIT_SERVER_ADDRESS=localhost
```

### Fichier de Configuration Streamlit

Créer `.streamlit/config.toml` :
```toml
[server]
port = 8501
address = "localhost"
enableCORS = false
enableXsrfProtection = false

[browser]
gatherUsageStats = false
```

## 🐛 Dépannage

### Problème : Python non trouvé
```bash
# Solution : Installer Python depuis python.org
# Vérifier PATH Windows
echo $PATH
```

### Problème : pip non trouvé
```bash
# Solution : Installer pip
python -m ensurepip --upgrade
```

### Problème : Erreur de dépendances
```bash
# Solution : Réinstaller les dépendances
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

### Problème : Port déjà utilisé
```bash
# Solution : Changer le port
streamlit run cacao1.py --server.port 8502
```

### Problème : Modèle non trouvé
```bash
# Solution : Régénérer le modèle
python train_model.py
```

## 📱 Installation Mobile (Optionnel)

### Streamlit Cloud
1. **Connecter** votre repository GitHub
2. **Déployer** automatiquement
3. **Accéder** via l'URL fournie

### Heroku
```bash
# Créer Procfile
echo "web: streamlit run cacao1.py --server.port=\$PORT" > Procfile

# Déployer
heroku create mon-cacao-app
git push heroku main
```

## 🔒 Sécurité

### Environnement de Production
- **Utiliser HTTPS** pour les connexions
- **Configurer** l'authentification
- **Limiter** l'accès aux ports
- **Sauvegarder** régulièrement les données

### Variables Sensibles
```bash
# Ne jamais commiter les clés secrètes
echo "SECRET_KEY=votre_cle_secrete" > .env
```

## 📊 Vérification Post-Installation

### Test de Fonctionnement
1. **Lancer l'application**
2. **Créer un compte test**
3. **Effectuer une prédiction**
4. **Vérifier les résultats**

### Tests Automatisés
```bash
# Créer un script de test
python -c "
import streamlit as st
import joblib
import pandas as pd
print('✅ Tous les modules sont installés correctement')
"
```

## 🆘 Support

### Ressources Utiles
- **Documentation Streamlit** : [docs.streamlit.io](https://docs.streamlit.io)
- **GitHub Issues** : [Issues](https://github.com/votre-username/mon-cacao/issues)
- **Stack Overflow** : Tag `streamlit`

### Contact
- **Email** : support@moncacao.ci
- **Discord** : [Serveur communautaire](https://discord.gg/moncacao)

---

**🌱 Installation réussie ! Votre application Mon Cacao est prête à l'emploi.**
