# 🌱 Mon Cacao - Frontend HTML

## Description

Ce frontend HTML moderne est conçu pour votre application de prédiction de productivité du cacao. Il offre une interface utilisateur élégante et responsive, optimisée pour les appareils mobiles avec un design adapté au format 3:3 pour Android.

## 🎨 Caractéristiques du Design

### Design Responsive
- **Format 3:3 pour Android** : Interface optimisée pour les écrans mobiles
- **Design moderne** : Utilisation de gradients, ombres et animations fluides
- **Thème cacao** : Couleurs vertes et dorées représentant la nature du cacao
- **Navigation fluide** : Menu hamburger pour mobile, navigation sticky

### Sections Principales

1. **Hero Section** : Présentation de l'application avec call-to-action
2. **Prédiction** : Formulaire interactif pour la prédiction de productivité
3. **Analytics** : Visualisations et statistiques
4. **À propos** : Informations sur l'application

## 🚀 Installation et Utilisation

### Prérequis
- Navigateur web moderne (Chrome, Firefox, Safari, Edge)
- Serveur web local (optionnel)

### Installation

1. **Ouvrir directement** :
   ```bash
   # Ouvrir le fichier index.html dans votre navigateur
   frontend/index.html
   ```

2. **Serveur local** (recommandé) :
   ```bash
   # Avec Python
   cd frontend
   python -m http.server 8000
   
   # Avec Node.js
   npx serve .
   
   # Avec PHP
   php -S localhost:8000
   ```

3. **Accéder à l'application** :
   - Ouvrez votre navigateur
   - Allez à `http://localhost:8000`

## 📱 Optimisations Mobile

### Format 3:3 pour Android
- **Grille responsive** : Adaptation automatique selon la taille d'écran
- **Navigation tactile** : Boutons et liens optimisés pour le touch
- **Performance** : Animations fluides et chargement rapide
- **Accessibilité** : Contraste élevé et tailles de police adaptées

### Breakpoints Responsive
- **Desktop** : > 768px
- **Tablet** : 768px - 480px
- **Mobile** : < 480px

## 🎯 Fonctionnalités

### Prédiction Interactive
- **Formulaire intelligent** : Validation en temps réel
- **Calculs automatiques** : Prédiction basée sur les données saisies
- **Visualisation** : Compteur circulaire animé
- **Recommandations** : Suggestions d'amélioration

### Analytics
- **Graphiques interactifs** : Prêts pour Chart.js
- **Statistiques en temps réel** : Métriques de performance
- **Filtres temporels** : Mois, trimestre, année

### Notifications
- **Système de notifications** : Feedback utilisateur
- **Types** : Succès, avertissement, erreur, info
- **Auto-dismiss** : Disparition automatique après 5 secondes

## 🛠️ Structure des Fichiers

```
frontend/
├── index.html          # Page principale
├── css/
│   └── style.css       # Styles CSS
├── js/
│   └── script.js       # Logique JavaScript
└── README.md           # Ce fichier
```

## 🎨 Personnalisation

### Couleurs
Les couleurs sont définies dans les variables CSS :
```css
:root {
    --primary-color: #2E8B57;      /* Vert principal */
    --secondary-color: #1a472a;    /* Vert foncé */
    --accent-color: #FFD700;       /* Or accent */
    --background-color: #f8f9fa;   /* Gris clair */
}
```

### Animations
- **Fade-in-up** : Apparition des éléments au scroll
- **Float** : Animation de flottement pour les cartes
- **Bounce** : Animation de rebond pour les icônes
- **Slide-in** : Notifications qui glissent

## 🔧 Intégration avec l'API

### Connexion au Backend
Pour connecter le frontend à votre API Streamlit :

1. **Modifier la fonction `predictProductivity()`** dans `script.js`
2. **Remplacer `simulatePrediction()`** par un appel API réel
3. **Adapter les endpoints** selon votre configuration

### Exemple d'intégration API
```javascript
async function predictProductivity() {
    const formData = {
        temperature: parseFloat(document.getElementById('temperature').value),
        humidity: parseFloat(document.getElementById('humidity').value),
        rainfall: parseFloat(document.getElementById('rainfall').value),
        soil_ph: parseFloat(document.getElementById('soil_ph').value),
        fertilizer: parseFloat(document.getElementById('fertilizer').value),
        pesticide: parseFloat(document.getElementById('pesticide').value)
    };

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        const result = await response.json();
        displayPredictionResult(result);
    } catch (error) {
        showNotification('Erreur de connexion', 'error');
    }
}
```

## 📊 Graphiques

### Chart.js Integration
Le frontend est préparé pour Chart.js. Pour l'activer :

1. **Installer Chart.js** :
   ```html
   <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
   ```

2. **Décommenter le code** dans `initializeCharts()` dans `script.js`

3. **Adapter les données** selon vos besoins

## 🧪 Tests

### Test des Fonctionnalités
1. **Navigation** : Vérifier le menu mobile et la navigation smooth
2. **Formulaire** : Tester la validation des champs
3. **Prédiction** : Vérifier les calculs et animations
4. **Responsive** : Tester sur différentes tailles d'écran

### Validation des Données
- **Température** : -10°C à 50°C
- **Humidité** : 0% à 100%
- **Précipitations** : ≥ 0 mm
- **pH du sol** : 0 à 14
- **Engrais/Pesticides** : ≥ 0 kg/ha

## 🚀 Déploiement

### Options de Déploiement
1. **GitHub Pages** : Déploiement gratuit
2. **Netlify** : Déploiement automatique
3. **Vercel** : Performance optimisée
4. **Serveur web** : Apache, Nginx

### Configuration pour Production
- **Minification** : CSS et JS
- **Optimisation images** : WebP, compression
- **Cache** : Headers appropriés
- **HTTPS** : Certificat SSL

## 🤝 Contribution

### Améliorations Suggérées
- [ ] Intégration complète avec Chart.js
- [ ] Mode sombre
- [ ] Internationalisation (i18n)
- [ ] Tests automatisés
- [ ] PWA (Progressive Web App)

### Standards de Code
- **CSS** : BEM methodology
- **JavaScript** : ES6+, async/await
- **HTML** : Sémantique, accessibilité
- **Performance** : Lazy loading, optimisations

## 📞 Support

Pour toute question ou problème :
- **Email** : contact@moncacao.com
- **Documentation** : Voir les commentaires dans le code
- **Issues** : Créer une issue sur GitHub

---

**Développé avec ❤️ pour l'agriculture intelligente du cacao**
