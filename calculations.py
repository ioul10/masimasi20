# ============================================
# CALCULS FINANCIERS - FUTURES MASI/MASI20
# ============================================

import numpy as np
import config

def calcul_valeur_notionnelle(prix_future, multiplicateur):
    """
    Calcule la valeur notionnelle d'un contrat future
    Document §4.3: Valeur = Prix Future × Taille du Contrat
    """
    return prix_future * multiplicateur

def calcul_nombre_contrats_optimal(portefeuille_value, beta, indice_niveau, multiplicateur):
    """
    Calcule le nombre optimal de contrats pour couverture
    Document §6.2: N* = β × P / A
    """
    valeur_notionnelle = calcul_valeur_notionnelle(indice_niveau, multiplicateur)
    n_star = beta * portefeuille_value / valeur_notionnelle
    return round(n_star)

def calcul_gain_perte_future(prix_entree, prix_sortie, nombre_contrats, multiplicateur):
    """
    Calcule le gain/perte sur une position future
    Document §4.2: Gain = (F_clôture − F_entrée) × Taille × N
    """
    variation = prix_sortie - prix_entree
    return variation * multiplicateur * nombre_contrats

def calcul_prix_future_theorique(spot, taux_sans_risque, rendement_dividende, maturite_annees):
    """
    Calcule le prix théorique d'un future sur indice
    Document §7.1: F₀ = S₀ × e^((r−q)T)
    """
    return spot * np.exp((taux_sans_risque - rendement_dividende) * maturite_annees)

def calcul_variation_portefeuille(portefeuille_value, beta, variation_indice_pct):
    """
    Calcule la variation d'un portefeuille selon son bêta
    Document §6: Variation = β × Variation Indice
    """
    return portefeuille_value * (1 + beta * variation_indice_pct / 100)

def calcul_marge_initiale(valeur_notionnelle, pourcentage=config.MarginConstants.MARGE_INITIALE_PCT):
    """Calcule la marge initiale requise"""
    return valeur_notionnelle * (pourcentage / 100)

def calcul_marge_maintenance(marge_initiale, pourcentage=config.MarginConstants.MARGE_MAINTENANCE_PCT):
    """Calcule le seuil de marge de maintenance"""
    return marge_initiale * (pourcentage / 100)

def calcul_appel_marge(solde_actuel, marge_maintenance, marge_initiale):
    """
    Calcule le montant d'appel de marge si nécessaire
    Document §5.1
    """
    if solde_actuel < marge_maintenance:
        return marge_initiale - solde_actuel
    return 0

def calcul_var_simple(portefeuille_value, volatilite_annuelle, niveau_confiance=0.95, horizon_jours=1):
    """
    Calcule la Value at Risk (VaR) paramétrique
    Document §1.2: VaR consolidée
    """
    z_score = 1.645 if niveau_confiance == 0.95 else 2.326
    volatilite_journaliere = volatilite_annuelle / np.sqrt(252)
    var = portefeuille_value * z_score * volatilite_journaliere * np.sqrt(horizon_jours)
    return var