# ============================================
# MASI FUTURES PRO SIMULATOR
# Point d'Entrée Principal
# ============================================

import streamlit as st
import config

# Configuration de la page Streamlit
st.set_page_config(
    page_title=config.STREAMLIT_CONFIG["page_title"],
    page_icon=config.STREAMLIT_CONFIG["page_icon"],
    layout=config.STREAMLIT_CONFIG["layout"],
    initial_sidebar_state=config.STREAMLIT_CONFIG["initial_sidebar_state"]
)

# ────────────────────────────────────────────
# STYLE CSS PERSONNALISÉ
# ────────────────────────────────────────────
st.markdown(f"""
    <style>
    .main {{
        background-color: {config.Colors.BACKGROUND};
    }}
    .stApp {{
        background-color: {config.Colors.BACKGROUND};
    }}
    h1, h2, h3 {{
        color: {config.Colors.PRIMARY};
        font-family: 'Segoe UI', sans-serif;
    }}
    .stSidebar {{
        background-color: {config.Colors.CARD_BACKGROUND};
    }}
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────
# HEADER & BRANDING
# ────────────────────────────────────────────
st.markdown(f"""
    <div style='background-color: {config.Colors.PRIMARY}; 
                padding: 20px; 
                border-radius: 10px; 
                margin-bottom: 20px;'>
        <h1 style='color: white; margin: 0;'>📈 {config.APP_NAME}</h1>
        <p style='color: #E0E0E0; margin: 5px 0 0 0;'>
            Version {config.APP_VERSION} | {config.APP_AUTHOR}
        </p>
    </div>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────
# SIDEBAR DE NAVIGATION
# ────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🧭 Navigation")
    
    # Sélecteur de profil utilisateur
    profil = st.selectbox(
        "👤 Profil Utilisateur",
        ["Étudiant", "Investisseur", "Trader", "Risk Manager", "Formateur"],
        help="Adapte l'interface selon votre profil"
    )
    
    st.divider()
    
    # Menu de navigation principal
    page_choice = st.radio(
        "Modules",
        [page["name"] for page in config.NAVIGATION_PAGES],
        label_visibility="collapsed"
    )
    
    st.divider()
    
    # Informations contextuelles
    st.markdown("### 📊 Marché MASI")
    st.info(f"Niveau de référence: {config.MASIConstants.NIVEAU_REFERENCE_MASI:,} pts")
    st.info(f"Multiplicateur: {config.MASIConstants.MULTIPLICATEUR_MASI} MAD/pt")
    st.info(f"Devise: {config.MASIConstants.DEVISE}")

# ────────────────────────────────────────────
# ROUTING VERS LES PAGES
# ────────────────────────────────────────────
# Note: Pour la Phase 1, nous affichons juste la page d'accueil
# Les autres pages seront créées dans les phases suivantes

st.markdown("""
    ### 🎯 Bienvenue sur MASI Futures Pro Simulator
    
    Cette application professionnelle vous permet de :
    
    - ✅ **Comprendre** les contrats futures sur indices MASI/MASI20
    - ✅ **Simuler** des stratégies de couverture de portefeuille
    - ✅ **Calculer** les prix théoriques et opportunités d'arbitrage
    - ✅ **Gérer** les marges et appels de marge
    - ✅ **Analyser** les risques (VaR, stress testing)
    
    ---
    
    ### 📚 Basé sur le document officiel CDG Capital
    
    Cette application reprend intégralement les concepts, formules et 
    exemples du document "Introduction des Contrats Futures sur les 
    Indices MASI et MASI20".
    
    ---
    
    ### 🚀 Sélectionnez un module dans la sidebar pour commencer !
""")

# ────────────────────────────────────────────
# FOOTER
# ────────────────────────────────────────────
st.markdown("---")
st.markdown(f"""
    <div style='text-align: center; color: {config.Colors.TEXT_MUTED}; font-size: 12px;'>
        {config.APP_NAME} v{config.APP_VERSION} | 
        Basé sur les spécifications du marché à terme marocain
    </div>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────
# ROUTING VERS LES PAGES
# ────────────────────────────────────────────

# Mapping des choix de navigation vers les pages
page_mapping = {
    "🏠 Accueil": "pages/01_Accueil.py",
    "📚 Comprendre les Futures": "pages/02_Comprendre_Futures.py",
    "🛡️ Simulateur de Couverture": "pages/03_Simulateur_Couverture.py",
    "💰 Pricing & Arbitrage": "pages/04_Pricing_Arbitrage.py",
    "⚠️ Gestion des Marges": "pages/05_Gestion_Marges.py",
    "📊 Risk Dashboard": "pages/06_Risk_Dashboard.py",
}

# Afficher la page sélectionnée
if page_choice in page_mapping:
    # Pour la Phase 2, seule la page 02 est complète
    if page_choice == "🏠 Accueil":
        # Contenu de la page d'accueil (déjà dans app.py)
        pass
    elif page_choice == "📚 Comprendre les Futures":
        # Import et exécution de la page 02
        exec(open("pages/02_Comprendre_Futures.py").read())
    else:
        st.info(f"🚧 Module '{page_choice}' en cours de développement - Disponible dans les prochaines phases")