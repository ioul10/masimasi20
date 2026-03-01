# ============================================
# GLOSSAIRE INTERACTIF - TERMES CLÉS
# Basé sur le document CDG Capital
# ============================================

GLOSSARY_TERMS = {
    "Marché à Terme": """
        **Définition :** Marché organisé sur lequel s'échangent des contrats futurs 
        standardisés portant sur un actif financier (indice boursier MASI/MASI20).
        
        **Caractéristiques :**
        • Contrats standardisés
        • Prix déterminé à l'avance
        • Échéance future prédéfinie
        • Sécurisation par une Chambre de Compensation (CCP)
        
        **Document :** Section 2.1
    """,
    
    "Future sur Indice": """
        **Définition :** Contrat permettant de prendre une position sur la performance 
        globale d'un indice boursier sans détenir directement les actions.
        
        **Utilisations :**
        • Couverture des portefeuilles actions
        • Prise d'exposition rapide
        • Arbitrage spot/future
        
        **Document :** Section 2.2
    """,
    
    "Cash Settlement": """
        **Définition :** Règlement en espèces à l'échéance du contrat, sans livraison 
        physique des actions composant l'indice.
        
        **Fonctionnement :**
        La différence entre le prix future et le niveau final de l'indice est 
        calculée et réglée en cash entre les parties.
        
        **Document :** Section 4.1.b & 4.2.b
    """,
    
    "Chambre de Compensation (CCP)": """
        **Définition :** Entité qui garantit la bonne exécution des engagements 
        entre les parties et sécurise les transactions.
        
        **Rôles :**
        • Réduction du risque de contrepartie
        • Gestion des marges
        • Compensation des positions
        
        **Document :** Section 2.1
    """,
    
    "Marking to Market": """
        **Définition :** Ajustement quotidien des gains et pertes sur les positions 
        futures en fonction de l'évolution du marché.
        
        **Fonctionnement :**
        Les pertes sont réglées progressivement au fur et à mesure des variations 
        du marché, réduisant ainsi le risque de contrepartie.
        
        **Document :** Section 5.1
    """,
    
    "Marge Initiale": """
        **Définition :** Dépôt initial exigé par la chambre de compensation à 
        l'ouverture d'une position.
        
        **Typique :** ~10% de la valeur notionnelle du contrat
        
        **Document :** Section 4.1.c & 5.1
    """,
    
    "Marge de Maintenance": """
        **Définition :** Seuil minimal du compte en dessous duquel un appel de 
        marge est déclenché.
        
        **Typique :** ~75% de la marge initiale
        
        **Document :** Section 5.1
    """,
    
    "Appel de Marge": """
        **Définition :** Demande de fonds supplémentaires lorsque le solde du 
        compte descend sous la marge de maintenance.
        
        **Conséquence :** Si non honoré, la position est automatiquement clôturée.
        
        **Document :** Section 5.1
    """,
    
    "Bêta (β)": """
        **Définition :** Mesure de la sensibilité d'un portefeuille aux variations 
        du marché (indice MASI/MASI20).
        
        **Interprétation :**
        • β = 1 : Portefeuille suit le marché
        • β > 1 : Portefeuille plus volatil que le marché
        • β < 1 : Portefeuille moins volatil que le marché
        
        **Document :** Section 6.2
    """,
    
    "Ratio de Couverture (N*)": """
        **Définition :** Nombre optimal de contrats futures nécessaires pour 
        couvrir un portefeuille.
        
        **Formule :** N* = β × P / A
        
        Où :
        • P = Valeur du portefeuille
        • A = Valeur notionnelle d'un contrat
        • β = Bêta du portefeuille
        
        **Document :** Section 6.2
    """,
    
    "Valeur Notionnelle": """
        **Définition :** Valeur totale du contrat future.
        
        **Formule :** Valeur = Prix Future × Taille du Contrat (Multiplicateur)
        
        **Exemple :** MASI 12 000 pts × 10 MAD = 120 000 MAD
        
        **Document :** Section 4.3
    """,
    
    "Limit Up / Limit Down": """
        **Définition :** Variations journalières maximales autorisées du prix 
        au cours d'une même séance.
        
        **Objectif :** Éviter les mouvements excessifs et préserver l'intégrité 
        du marché.
        
        **Document :** Section 4.4.a
    """,
    
    "Limites de Position": """
        **Définition :** Nombre maximal de contrats qu'un intervenant peut détenir.
        
        **Objectifs :**
        • Éviter l'influence excessive d'un acteur unique
        • Réduire les risques de manipulation
        • Préserver la liquidité
        
        **Document :** Section 4.4.c
    """,
    
    "Convergence des Prix": """
        **Définition :** À l'approche de l'échéance, le prix future converge 
        vers le prix spot de l'indice.
        
        **Principe :** Si ce n'était pas le cas, des opportunités d'arbitrage 
        apparaîtraient.
        
        **Document :** Section 4.5
    """,
    
    "Prix Future Théorique": """
        **Définition :** Prix théorique d'un contrat future selon la relation 
        d'absence d'arbitrage.
        
        **Formule :** F₀ = S₀ × e^((r−q)T)
        
        Où :
        • S₀ = Niveau spot de l'indice
        • r = Taux sans risque
        • q = Rendement en dividendes
        • T = Maturité en années
        
        **Document :** Section 7.1
    """,
    
    "Arbitrage": """
        **Définition :** Stratégie permettant de réaliser un profit sans risque 
        en exploitant les écarts de prix entre marchés.
        
        **Stratégies :**
        • Si F_market > F_théorique : Achat spot + Vente future
        • Si F_market < F_théorique : Vente spot + Achat future
        
        **Document :** Section 7.2
    """,
    
    "VaR (Value at Risk)": """
        **Définition :** Mesure statistique du risque de perte d'un portefeuille 
        sur un horizon donné avec un niveau de confiance.
        
        **Utilisation :** Intégrée dans les dispositifs internes de gestion 
        des risques.
        
        **Document :** Section 1.2
    """,
    
    "CDG Capital - 4 Rôles": """
        **Définition :** Positionnement intégré de CDG Capital sur le marché 
        à terme.
        
        **Rôles :**
        1. Investisseur (trading pour compte propre)
        2. Négociateur (fonction marché)
        3. Compensateur (fonction marché)
        4. Gestionnaire Post-Trade (délégataire)
        
        **Document :** Section 3
    """,
}

def get_glossary_term(term):
    """Récupère la définition d'un terme du glossaire"""
    return GLOSSARY_TERMS.get(term, "Terme non trouvé dans le glossaire.")

def get_all_terms():
    """Retourne la liste de tous les termes du glossaire"""
    return list(GLOSSARY_TERMS.keys())