#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vérification de la modification du label de prix dans la page prediction
"""

import os

def verifier_modification_prix():
    """Vérifier que la modification du label de prix a été appliquée"""
    
    print("🔍 VÉRIFICATION DE LA MODIFICATION DU PRIX")
    print("=" * 50)
    
    html_file = "frontend/prediction.html"
    
    if not os.path.exists(html_file):
        print(f"❌ Fichier {html_file} non trouvé")
        return False
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Erreur lecture HTML : {e}")
        return False
    
    # Vérifications à effectuer
    tests = []
    
    # Test 1: Label modifié
    label_modifie = 'Prix de vente du cacao (Fcfa/Kg)' in content
    tests.append(label_modifie)
    print(f"✅ Label modifié : {'✅' if label_modifie else '❌'}")
    
    # Test 2: Ancien label supprimé
    ancien_label = 'Prix de vente (FCFA/tonne)' in content
    tests.append(not ancien_label)
    print(f"✅ Ancien label supprimé : {'✅' if not ancien_label else '❌'}")
    
    # Test 3: Valeur par défaut modifiée
    valeur_modifiee = 'value="1000"' in content
    tests.append(valeur_modifiee)
    print(f"✅ Valeur par défaut modifiée : {'✅' if valeur_modifiee else '❌'}")
    
    # Test 4: Placeholder modifié
    placeholder_modifie = 'placeholder="1000"' in content
    tests.append(placeholder_modifie)
    print(f"✅ Placeholder modifié : {'✅' if placeholder_modifie else '❌'}")
    
    # Test 5: Ancienne valeur supprimée
    ancienne_valeur = 'value="750000"' in content
    tests.append(not ancienne_valeur)
    print(f"✅ Ancienne valeur supprimée : {'✅' if not ancienne_valeur else '❌'}")
    
    # Résumé
    print("\n" + "=" * 50)
    print("🎯 RÉSULTAT DE LA VÉRIFICATION")
    print("=" * 50)
    
    passed = sum(tests)
    total = len(tests)
    
    print(f"✅ Tests réussis : {passed}/{total}")
    print(f"📈 Taux de réussite : {(passed/total)*100:.1f}%")
    
    if passed == total:
        print("\n🎉 SUCCÈS : MODIFICATION CORRECTEMENT APPLIQUÉE !")
        print("\n📋 DÉTAILS DE LA MODIFICATION :")
        print("   ✅ Label : 'Prix de vente du cacao (Fcfa/Kg)'")
        print("   ✅ Valeur par défaut : 1000")
        print("   ✅ Placeholder : 1000")
        print("   ✅ Anciens éléments supprimés")
        return True
    else:
        print(f"\n⚠️  {total-passed} problème(s) détecté(s)")
        return False

def main():
    """Fonction principale"""
    print("🚀 DÉMARRAGE DE LA VÉRIFICATION")
    print("=" * 50)
    
    success = verifier_modification_prix()
    
    if success:
        print("\n🎉 CONFIRMATION : LA MODIFICATION A ÉTÉ APPLIQUÉE !")
        print("\n📝 RÉSUMÉ :")
        print("   ✅ Le label affiche maintenant 'Prix de vente du cacao (Fcfa/Kg)'")
        print("   ✅ La valeur par défaut est 1000 Fcfa/Kg")
        print("   ✅ L'interface est plus claire et précise")
        return True
    else:
        print("\n⚠️  ATTENTION : La modification nécessite une vérification")
        return False

if __name__ == "__main__":
    main()
