# ============================================
# CONFIGURATION GLOBALE - MASI FUTURES PRO
# ============================================

# ────────────────────────────────────────────
# 1. PARAMÈTRES DE L'APPLICATION
# ────────────────────────────────────────────
APP_NAME = "MASI Futures Pro Simulator"
APP_VERSION = "1.0.0"
APP_AUTHOR = "CDG Capital - Formation"

# ────────────────────────────────────────────
# 2. COULEURS & THÈME (Palette Institutionnelle)
# ────────────────────────────────────────────
class Colors:
    PRIMARY = "#003366"        # Bleu institutionnel
    SECONDARY = "#0066CC"      # Bleu clair
    ACCENT = "#0099FF"         # Bleu accent
    SUCCESS = "#28A745"        # Vert (gain)
    DANGER = "#DC3545"         # Rouge (perte)
    WARNING = "#FFC107"        # Jaune (attention)
    BACKGROUND = "#F8F9FA"     # Fond clair
    TEXT = "#212529"           # Texte principal
    TEXT_MUTED = "#6C757D"     # Texte secondaire
    CARD_BACKGROUND = "#FFFFFF"  # Fond des cartes

# ────────────────────────────────────────────
# 3. CONSTANTES MASI / MASI20 (Document §4.1)
# ────────────────────────────────────────────
class MASIConstants:
    # Multiplicateur standard (à ajuster selon spécifications officielles)
    MULTIPLICATEUR_MASI = 10  # MAD par point d'indice
    MULTIPLICATEUR_MASI20 = 10  # MAD par point d'indice
    
    # Niveaux de référence (exemple du document §6)
    NIVEAU_REFERENCE_MASI = 12000  # points
    
    # Devises
    DEVISE = "MAD"
    DEVISE_SYMBOLE = "DH"
    
    # Échéances standardisées
    ECHEANCES = ["Mensuelle", "Trimestrielle"]
    
    # Limites de marché (Document §4.4)
    LIMIT_UP_DOWN_DEFAULT = 10  # % variation journalière max

# ────────────────────────────────────────────
# 4. PARAMÈTRES DE MARGE (Document §5.1)
# ────────────────────────────────────────────
class MarginConstants:
    MARGE_INITIALE_PCT = 10  # % de la valeur notionnelle
    MARGE_MAINTENANCE_PCT = 75  # % de la marge initiale
    MARKING_TO_MARKET = True  # Ajustement quotidien

# ────────────────────────────────────────────
# 5. PARAMÈTRES DE PRICING (Document §7.1)
# ────────────────────────────────────────────
class PricingConstants:
    TAUX_SANS_RISQUE_DEFAULT = 0.03  # 3% annuel
    DIVIDENDE_YIELD_DEFAULT = 0.025  # 2.5% annuel
    JOURS_PAR_AN = 252  # Jours de trading

# ────────────────────────────────────────────
# 6. SOURCES DE DONNÉES
# ────────────────────────────────────────────
class DataSource:
    MODE = "mock"  # Options: "mock", "scraping", "api"
    
    # URLs officielles (Document §4)
    BOURSE_CASABLANCA_URL = "https://www.casablanca-bourse.com"
    AMMC_URL = "https://www.ammc.ma"
    
    # Chemins de fichiers locaux
    DATA_DIR = "data"
    MASI_HISTORICAL_FILE = "data/masi_historical.csv"
    DIVIDEND_CALENDAR_FILE = "data/dividend_calendar.csv"

# ────────────────────────────────────────────
# 7. EXPORT & REPORTING
# ────────────────────────────────────────────
class ExportConfig:
    SUPPORTED_FORMATS = ["PDF", "Excel", "CSV"]
    DEFAULT_FORMAT = "PDF"
    REPORT_TEMPLATE = "professional"

# ────────────────────────────────────────────
# 8. NAVIGATION (6 Modules du Document)
# ────────────────────────────────────────────
NAVIGATION_PAGES = [
    {"id": "01", "name": "🏠 Accueil", "file": "pages/01_Accueil.py"},
    {"id": "02", "name": "📚 Comprendre les Futures", "file": "pages/02_Comprendre_Futures.py"},
    {"id": "03", "name": "🛡️ Simulateur de Couverture", "file": "pages/03_Simulateur_Couverture.py"},
    {"id": "04", "name": "💰 Pricing & Arbitrage", "file": "pages/04_Pricing_Arbitrage.py"},
    {"id": "05", "name": "⚠️ Gestion des Marges", "file": "pages/05_Gestion_Marges.py"},
    {"id": "06", "name": "📊 Risk Dashboard", "file": "pages/06_Risk_Dashboard.py"},
]

# ────────────────────────────────────────────
# 9. RÔLES CDG CAPITAL (Document §3)
# ────────────────────────────────────────────
CDG_ROLES = [
    "Investisseur (Trading pour compte propre)",
    "Négociateur (Fonction marché)",
    "Compensateur (Fonction marché)",
    "Gestionnaire Post-Trade (Délégataire)"
]

# ────────────────────────────────────────────
# 10. CONFIGURATION STREAMLIT
# ────────────────────────────────────────────
STREAMLIT_CONFIG = {
    "page_title": APP_NAME,
    "page_icon": "📈",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
    "menu_items": {
        "À propos": f"""
            **{APP_NAME}** v{APP_VERSION}
            
            Application professionnelle pour la simulation 
            de contrats futures sur indices MASI/MASI20.
            
            Basé sur le document officiel CDG Capital.
            """
    }
}