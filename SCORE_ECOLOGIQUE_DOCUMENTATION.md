# 🌍 Score Écologique - Mon Cacao

## 🎯 Vue d'ensemble

Le **Score Écologique** est une fonctionnalité innovante qui permet aux producteurs de cacao d'évaluer l'impact environnemental de leur plantation et de recevoir des recommandations personnalisées pour améliorer leurs pratiques agricoles.

## 🚀 Fonctionnalités Principales

### 1. **Évaluation Environnementale**
- **10 indicateurs** environnementaux clés
- **Système de notation** intuitif (sliders et boutons)
- **Calcul automatique** du score écologique
- **Classement par couleurs** : Rouge, Orange, Vert, Or

### 2. **Indicateurs Évalués**

#### 🌳 **Arbres d'ombrage (0-3)**
- **Niveau 0** : Aucun arbre d'ombrage
- **Niveau 1** : Quelques arbres dispersés
- **Niveau 2** : Ombrage partiel bien réparti
- **Niveau 3** : Ombrage dense et optimal

#### 🌱 **Couverture du sol (0-2)**
- **Niveau 0** : Sol nu, risque d'érosion
- **Niveau 1** : Couverture partielle
- **Niveau 2** : Couverture végétale complète

#### 🧪 **Fertilisation (0-3)**
- **Niveau 0** : Aucune fertilisation
- **Niveau 1** : Engrais chimiques uniquement
- **Niveau 2** : Mélange organique/chimique
- **Niveau 3** : Fertilisation 100% organique

#### 🛡️ **Pesticides (0-3)**
- **Niveau 0** : Utilisation intensive
- **Niveau 1** : Utilisation modérée
- **Niveau 2** : Utilisation minimale
- **Niveau 3** : Aucun pesticide (lutte biologique)

#### ✂️ **Taille sanitaire (0-3)**
- **Niveau 0** : Aucune taille
- **Niveau 1** : Taille occasionnelle
- **Niveau 2** : Taille régulière
- **Niveau 3** : Programme de taille optimisé

#### 💧 **Protection berges (0/1)**
- **Non** : Pas de protection des cours d'eau
- **Oui** : Zones tampons et protection des berges

#### ♻️ **Gestion déchets (0/1)**
- **Non** : Déchets agricoles non gérés
- **Oui** : Compostage et recyclage des déchets

#### 🐦 **Biodiversité (0-2)**
- **Niveau 0** : Monoculture pure
- **Niveau 1** : Quelques espèces associées
- **Niveau 2** : Écosystème diversifié

#### 🚫 **Déforestation (0/1)**
- **Non** : Déforestation récente
- **Oui** : Aucune déforestation

#### ✅ **Certification (0/1)**
- **Non** : Aucune certification
- **Oui** : Certification environnementale

## 🧮 Algorithme de Calcul

### Formule Pondérée
```
Score = (Σ(Valeur_indicateur × Poids_indicateur) / Score_maximum) × 100
```

### Poids par Indicateur
| Indicateur | Poids | Max | Impact |
|------------|-------|-----|--------|
| Fertilisation | 15 | 45 | 15% |
| Arbres d'ombrage | 12 | 36 | 12% |
| Pesticides | 12 | 36 | 12% |
| Biodiversité | 10 | 20 | 10% |
| Couverture du sol | 10 | 20 | 10% |
| Taille sanitaire | 10 | 30 | 10% |
| Gestion déchets | 8 | 8 | 8% |
| Protection berges | 8 | 8 | 8% |
| Déforestation | 8 | 8 | 8% |
| Certification | 7 | 7 | 7% |

### Seuils de Classification
- 🔴 **Rouge** : < 40 points (Critique)
- 🟠 **Orange** : 40-69 points (Moyen)
- 🟢 **Vert** : 70-84 points (Bon)
- 🟡 **Or** : ≥ 85 points (Excellent)

## 💾 Système de Stockage

### LocalStorage
```javascript
// Structure des données
{
  "ecoScoreHistory": [
    {
      "date": "01/01/2024",
      "time": "14:30",
      "score": 75,
      "level": "Bon",
      "color": "green"
    }
  ]
}
```

### Historique
- **10 derniers scores** conservés
- **Date et heure** de chaque évaluation
- **Niveau et couleur** associés
- **Accès rapide** aux tendances

## 🎨 Interface Utilisateur

### Design Moderne
- **Gradients verts** pour l'identité écologique
- **Cartes interactives** avec effets de survol
- **Sliders fluides** pour les niveaux
- **Boutons toggle** pour les indicateurs binaires
- **Badges colorés** pour les scores

### Responsive Design
- **Mobile-first** approach
- **Grille flexible** adaptative
- **Navigation intuitive**
- **Optimisation tactile**

### Animations
- **Entrée progressive** des éléments
- **Transitions fluides** entre états
- **Feedback visuel** des interactions
- **Effets de survol** élégants

## 📈 Recommandations Intelligentes

### Système de Suggestions
- **Analyse automatique** des points faibles
- **Recommandations prioritaires** (max 3)
- **Actions concrètes** et réalisables
- **Progression guidée** vers l'excellence

### Exemples de Recommandations
- 🌳 "Augmentez la densité des arbres d'ombrage"
- 🌱 "Implémentez une couverture végétale du sol"
- 🧪 "Privilégiez les engrais organiques"
- 🛡️ "Réduisez l'utilisation de pesticides"
- 🐦 "Créez des zones de refuge pour la biodiversité"

## 🔗 Intégration

### Navigation
- **Carte dédiée** dans la grille principale
- **Icône distinctive** (feuille verte)
- **Badge "Nouveau"** pour la visibilité
- **Retour facile** vers l'accueil

### Cohérence Visuelle
- **Design system** unifié
- **Couleurs cohérentes** avec l'application
- **Typographie harmonieuse**
- **Espacement standardisé**

## 🚀 Avantages

### Pour le Producteur
- **Awareness environnemental** accru
- **Amélioration progressive** des pratiques
- **Valorisation** des efforts écologiques
- **Conformité** aux standards internationaux

### Pour l'Environnement
- **Réduction** de l'impact écologique
- **Préservation** de la biodiversité
- **Gestion durable** des ressources
- **Contribution** à la lutte climatique

### Pour le Marché
- **Différenciation** des produits
- **Certification** facilitée
- **Accès** aux marchés premium
- **Réputation** environnementale

## 📊 Métriques de Performance

### Indicateurs Techniques
- ✅ **10 indicateurs** environnementaux
- ✅ **4 niveaux** de classification
- ✅ **Historique** de 10 évaluations
- ✅ **Interface** 100% responsive

### Indicateurs Utilisateur
- ✅ **Calcul instantané** du score
- ✅ **Recommandations** personnalisées
- ✅ **Navigation intuitive**
- ✅ **Feedback visuel** immédiat

## 🔮 Évolutions Futures

### Fonctionnalités Prévues
- **Comparaison** entre producteurs
- **Benchmarking** régional
- **Alertes** de dégradation
- **Intégration IA** pour recommandations avancées

### Améliorations Techniques
- **API REST** pour synchronisation
- **Base de données** cloud
- **Notifications** push
- **Export PDF** des rapports

### Intégrations
- **Certifications** automatiques
- **Marchés** de niche
- **Partenaires** environnementaux
- **Programmes** de compensation carbone

## 🎯 Objectifs Environnementaux

### Impact Mesurable
- **Réduction** de 30% des pesticides
- **Augmentation** de 50% de la biodiversité
- **Amélioration** de 40% de la fertilité des sols
- **Protection** de 100% des cours d'eau

### Objectifs de Développement Durable
- **ODD 12** : Consommation et production responsables
- **ODD 13** : Mesures relatives à la lutte contre les changements climatiques
- **ODD 15** : Vie terrestre
- **ODD 17** : Partenariats pour la réalisation des objectifs

---

**🌍 Le Score Écologique transforme la cacaoculture en pratique durable !**
