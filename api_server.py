from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os
import numpy as np

app = Flask(__name__)
CORS(app)  # Permet les requêtes cross-origin pour le frontend

# Charger le modèle XGBoost
MODEL_PATH = "model_productivite_xgb.pkl"
xgb_model = joblib.load(MODEL_PATH)

@app.route('/')
def home():
    return jsonify({
        "message": "API Mon Cacao - Modèle XGBoost",
        "version": "1.0",
        "endpoints": {
            "predict": "/predict",
            "health": "/health",
            "model_info": "/model-info"
        }
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "model_loaded": True})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupérer les données du frontend
        data = request.get_json()
        
        # Validation des données - mêmes paramètres que Streamlit
        required_fields = [
            'age_verger', 'agroforest', 'engrais', 'fumier', 'maladie',
            'herbicide', 'insecticide', 'fongicide', 'cout_prod', 'prix_a',
            'region', 'pluviometrie', 'sexe', 'competences'
        ]
        
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Champ manquant: {field}"}), 400
        
        # Création du dictionnaire de données - EXACTEMENT comme dans Streamlit
        model_data = {
            "Coût_production/ha": [data['cout_prod']],
            "Age_verger": [data['age_verger']],
            "Région": [data['region']],
            "Pluviometrie": [data['pluviometrie']],
            "Sexe": [data['sexe']],
            "Niveau_education": ["Non renseigné"],  # Valeur par défaut comme dans Streamlit
            "Competences": [data['competences']],
            "Engrais chimique": [data['engrais']],
            "Agroforesterie": [data['agroforest']],
            "fumier/ compost": [data['fumier']],
            "Herbicide": [data['herbicide']],
            "Insecticide": [data['insecticide']],
            "Fongicide": [data['fongicide']],
            "Maladie": [data['maladie']],
        }
        
        # Création du DataFrame et prédiction - EXACTEMENT comme dans Streamlit
        df_input = pd.DataFrame(model_data)
        X_trans = xgb_model.named_steps["prep"].transform(df_input)
        pred = xgb_model.named_steps["model"].predict(X_trans)[0]
        
        # Variables pour les calculs - EXACTEMENT comme dans Streamlit
        production = pred  # t/ha
        production_kg = production * 1000  # Conversion en kg/ha
        prix_vente = data['prix_a'] / 1000  # Conversion tonne vers kg (FCFA/kg)
        revenu = round(production_kg * prix_vente)  # FCFA/ha
        benefice = round(revenu - data['cout_prod'])  # FCFA/ha
        
        # Calcul de la confiance basé sur la cohérence des données
        confidence = calculate_confidence(data)
        
        # Recommandations basées sur la prédiction
        recommendation = get_recommendation(production, data)
        
        return jsonify({
            "success": True,
            "prediction": {
                "productivity_t_ha": round(production, 3),
                "productivity_kg_ha": round(production_kg),
                "revenue_fcfa": revenu,
                "benefit_fcfa": benefice,
                "confidence": confidence,
                "recommendation": recommendation,
                "price_per_kg": prix_vente,
                "cost_per_ha": data['cout_prod']
            },
            "input_data": data,
            "model_info": {
                "model_type": "XGBoost",
                "features_used": list(model_data.keys())
            }
        })
        
    except Exception as e:
        return jsonify({
            "error": f"Erreur lors de la prédiction: {str(e)}",
            "success": False
        }), 500

def calculate_confidence(data):
    """Calcule un score de confiance basé sur la qualité des données"""
    confidence = 85  # Base de 85%
    
    # Vérifier les plages de valeurs logiques
    if 0 <= data['age_verger'] <= 50:
        confidence += 5
    if data['cout_prod'] > 0:
        confidence += 5
    if data['prix_a'] > 0:
        confidence += 5
    
    return min(confidence, 95)  # Maximum 95%

def get_recommendation(prediction, data):
    """Génère des recommandations basées sur la prédiction et les données"""
    recommendations = []
    
    # Recommandations basées sur la productivité
    if prediction < 0.8:
        recommendations.append("Productivité faible - Optimisez l'utilisation des engrais")
        recommendations.append("Vérifiez l'état sanitaire des plants")
    elif prediction > 1.2:
        recommendations.append("Excellente productivité - Maintenez vos bonnes pratiques")
    else:
        recommendations.append("Productivité moyenne - Quelques améliorations possibles")
    
    # Recommandations basées sur les pratiques
    if data['engrais'] == "Non":
        recommendations.append("Envisagez l'utilisation d'engrais pour améliorer la productivité")
    
    if data['agroforest'] == "Non":
        recommendations.append("L'agroforesterie peut améliorer la résilience de votre plantation")
    
    if data['maladie'] != "Non":
        recommendations.append("Surveillez et traitez les maladies pour maintenir la productivité")
    
    return "; ".join(recommendations[:3])  # Limiter à 3 recommandations

@app.route('/model-info')
def model_info():
    """Retourne des informations sur le modèle"""
    return jsonify({
        "model_type": "XGBoost",
        "features": [
            "Coût_production/ha",
            "Age_verger", 
            "Région",
            "Pluviometrie",
            "Sexe",
            "Niveau_education",
            "Competences",
            "Engrais chimique",
            "Agroforesterie",
            "fumier/ compost",
            "Herbicide",
            "Insecticide",
            "Fongicide",
            "Maladie"
        ],
        "output": "Productivité (t/ha)",
        "preprocessing": "StandardScaler + OneHotEncoder",
        "streamlit_compatible": True
    })

@app.route('/streamlit-params')
def streamlit_params():
    """Retourne les paramètres attendus par l'API (même que Streamlit)"""
    return jsonify({
        "required_parameters": {
            "age_verger": "float - Âge du verger (années)",
            "agroforest": "string - Agroforesterie (Oui/Non)",
            "engrais": "string - Engrais chimique (Oui/Non)",
            "fumier": "string - Fumier/Compost (Oui/Non)",
            "maladie": "string - Présence de maladies (Non/oui/Un peu)",
            "herbicide": "string - Utilisation d'herbicides (Oui/Non)",
            "insecticide": "string - Utilisation d'insecticides (Oui/Non)",
            "fongicide": "string - Utilisation de fongicides (Oui/Non)",
            "cout_prod": "float - Coût de production (FCFA/ha)",
            "prix_a": "float - Prix d'achat (FCFA/tonne)",
            "region": "string - Région (Indenie-Djuablin/Yamoussoukro/La Me/San-Pedro/Grand-Ponts)",
            "pluviometrie": "string - Niveau de pluviométrie (Faible/Moyenne/Élevée)",
            "sexe": "string - Genre (Masculin/Feminin)",
            "competences": "string - Niveau d'alphabétisation (oui, lire et écrire/oui, lire seulement/non)"
        },
        "example_request": {
            "age_verger": 15.0,
            "agroforest": "Non",
            "engrais": "Oui",
            "fumier": "Non",
            "maladie": "Non",
            "herbicide": "Non",
            "insecticide": "Oui",
            "fongicide": "Non",
            "cout_prod": 450000.0,
            "prix_a": 750000.0,
            "region": "Indenie-Djuablin",
            "pluviometrie": "Moyenne",
            "sexe": "Masculin",
            "competences": "oui, lire et écrire"
        }
    })

if __name__ == '__main__':
    print("🌱 Démarrage de l'API Mon Cacao...")
    print(f"📦 Modèle chargé: {MODEL_PATH}")
    print("🚀 Serveur API disponible sur http://localhost:5000")
    print("📋 Paramètres identiques à l'application Streamlit")
    app.run(debug=True, host='0.0.0.0', port=5000)
