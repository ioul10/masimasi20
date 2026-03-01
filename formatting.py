# ============================================
# UTILITAIRES DE FORMATAGE FINANCIER
# ============================================

import config
from datetime import datetime

def format_mad(amount, decimals=2):
    """Formate un montant en MAD (Document §4.1)"""
    return f"{amount:,.{decimals}f} {config.MASIConstants.DEVISE_SYMBOLE}"

def format_points(points, decimals=2):
    """Formate un niveau d'indice en points"""
    return f"{points:,.{decimals}f} pts"

def format_percentage(value, decimals=2):
    """Formate un pourcentage"""
    return f"{value:.{decimals}f}%"

def format_date(date_obj):
    """Formate une date en format français"""
    if isinstance(date_obj, str):
        date_obj = datetime.strptime(date_obj, "%Y-%m-%d")
    return date_obj.strftime("%d/%m/%Y")

def format_number(number, decimals=0):
    """Formate un nombre avec séparateurs de milliers"""
    return f"{number:,.{decimals}f}"

def format_contract_value(price, multiplier):
    """Calcule et formate la valeur notionnelle d'un contrat (Document §4.3)"""
    value = price * multiplier
    return format_mad(value)

def colorize_pnl(value):
    """Retourne une couleur selon le P&L (vert=gain, rouge=perte)"""
    if value > 0:
        return "green"
    elif value < 0:
        return "red"
    else:
        return "gray"

def format_pnl_html(value):
    """Formate un P&L avec couleur pour affichage HTML"""
    color = colorize_pnl(value)
    sign = "+" if value > 0 else ""
    return f"<span style='color: {color}; font-weight: bold;'>{sign}{format_mad(value)}</span>"