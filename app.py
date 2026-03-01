# ============================================
# MASI FUTURES PRO SIMULATOR
# Point d'Entrée Principal (Page d'Accueil)
# ============================================

import streamlit as st
import config

# ────────────────────────────────────────────
# CONFIGURATION DE LA PAGE
# ────────────────────────────────────────────
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
    .metric-card {{
        background-color: {config.Colors.CARD_BACKGROUND};
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid {config.Colors.PRIMARY};
        margin: 10px 0;
    }}
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────
# HEADER & BRANDING
# ────────────────────────────────────────────
st.markdown(f"""
    <div style='background: linear-gradient(135deg, {config.Colors.PRIMARY}, {config.Colors.SECONDARY}); 
                padding: 25px; 
                border-radius: 12px; 
                margin-bottom: 25px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h1 style='color: white; margin: 0; font-size: 1.8em;'>📈 {config.APP_NAME}</h1>
        <p style='color: #E0E0E0; margin: 8px 0 0 0; font-size: 1.1em;'>
            Version {config.APP_VERSION} | {config.APP_AUTHOR}
        </p>
    </div>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────
# SIDEBAR - CONFIGURATION UTILISATEUR
# ────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🧭 Navigation")
    
    # Sélecteur de profil utilisateur (persistant via session state)
    if 'user_profile' not in st.session_state:
        st.session_state.user_profile = "Investisseur"
    
    profil = st.selectbox(
        "👤 Profil Utilisateur",
        ["Étudiant", "Investisseur", "Trader", "Risk Manager", "Formateur"],
        index=["Étudiant", "Investisseur", "Trader", "Risk Manager", "Formateur"].index(st.session_state.user_profile),
        help="Adapte l'interface selon votre profil"
    )
    st.session_state.user_profile = profil
    
    st.divider()
    
    # Informations contextuelles MASI
    st.markdown("### 📊 Marché MASI")
    
    with st.container(border=True):
        st.metric(
            label="Niveau de référence",
            value=f"{config.MASIConstants.NIVEAU_REFERENCE_MASI:,} pts",
            delta=None
        )
        st.metric(
            label="Multiplicateur",
            value=f"{config.MASIConstants.MULTIPLICATEUR_MASI} MAD/pt",
            delta=None
        )
        st.metric(
            label="Devise",
            value=config.MASIConstants.DEVISE,
            delta=None
        )
    
    st.divider()
    
    # Liens utiles
    st.markdown("### 🔗 Ressources")
    st.markdown(f"""
        - [📄 Document CDG Capital](#)
        - [🌐 Bourse de Casablanca](https://www.casablanca-bourse.com)
        - [📊 AMMC](https://www.ammc.ma)
    """)

# ────────────────────────────────────────────
# CONTENU PRINCIPAL - PAGE D'ACCUEIL
# ────────────────────────────────────────────

# Section Hero
st.markdown("""
    ### 🎯 Bienvenue sur MASI Futures Pro Simulator
    
    Cette application professionnelle vous permet de maîtriser les contrats 
    futures sur indices **MASI** et **MASI20** du marché marocain.
""")

# Cartes de fonctionnalités
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div class='metric-card'>
            <h4 style='margin: 0 0 10px 0; color: {config.Colors.PRIMARY};'>📚 Apprendre</h4>
            <p style='margin: 0; font-size: 0.95em;'>
                Comprendre les concepts clés : marché à terme, couverture, pricing, gestion des marges
            </p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class='metric-card'>
            <h4 style='margin: 0 0 10px 0; color: {config.Colors.PRIMARY};'>🛡️ Simuler</h4>
            <p style='margin: 0; font-size: 0.95em;'>
                Tester des stratégies de couverture avec calculateur N* = β × P/A
            </p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class='metric-card'>
            <h4 style='margin: 0 0 10px 0; color: {config.Colors.PRIMARY};'>📊 Analyser</h4>
            <p style='margin: 0; font-size: 0.95em;'>
                Évaluer les risques (VaR, stress testing) et générer des rapports
            </p>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# Modules disponibles
st.markdown("### 🚀 Modules Disponibles")

modules = [
    {
        "icon": "📚",
        "title": "Comprendre les Futures",
        "desc": "Contenu éducatif complet basé sur le document CDG Capital",
        "page": "pages/02_Comprendre_Futures.py",
        "status": "✅ Disponible"
    },
    {
        "icon": "🛡️",
        "title": "Simulateur de Couverture",
        "desc": "Calcul du ratio optimal N* = β × P/A avec visualisation P&L",
        "page": "pages/03_Simulateur_Couverture.py",
        "status": "🚧 En développement"
    },
    {
        "icon": "💰",
        "title": "Pricing & Arbitrage",
        "desc": "Calcul du prix théorique F₀ = S₀·e^((r−q)T) et détection d'opportunités",
        "page": "pages/04_Pricing_Arbitrage.py",
        "status": "🚧 En développement"
    },
    {
        "icon": "⚠️",
        "title": "Gestion des Marges",
        "desc": "Simulation du marking-to-market et des appels de marge",
        "page": "pages/05_Gestion_Marges.py",
        "status": "🚧 En développement"
    },
    {
        "icon": "📊",
        "title": "Risk Dashboard",
        "desc": "Analyse VaR, CVaR, stress testing et export de rapports",
        "page": "pages/06_Risk_Dashboard.py",
        "status": "🚧 En développement"
    }
]

for module in modules:
    with st.expander(f"{module['icon']} **{module['title']}** — {module['status']}", expanded=(module['title']=="Comprendre les Futures")):
        st.markdown(f"*{module['desc']}*")
        if module['status'] == "✅ Disponible":
            st.page_link(module['page'], label="➡️ Accéder au module", icon="🔗")
        else:
            st.caption("Ce module sera disponible dans les prochaines phases de développement.")

st.divider()

# Section Référence Document
st.markdown("### 📖 Référence Documentaire")

st.info("""
    **Source :** *"Introduction des Contrats Futures sur les Indices MASI et MASI20"*
    
    **Éditeur :** CDG Capital
    
    **Contenu couvert :**
    - ✅ Objectifs généraux et gestion des risques
    - ✅ Définitions et fonctionnement des marchés à terme
    - ✅ Formules de pricing et de couverture
    - ✅ Mécanismes de marge et régulation
    - ✅ Exemples chiffrés et cas pratiques
""")

# Section Profil Utilisateur - Contenu Adapté
st.markdown("### 👤 Contenu Adapté à Votre Profil")

profile_content = {
    "Étudiant": """
        🎓 **Parcours recommandé :**
        1. Commencez par le module "Comprendre les Futures"
        2. Utilisez le glossaire interactif pour les termes techniques
        3. Validez vos connaissances avec le quiz
        4. Explorez les simulateurs pour appliquer la théorie
    """,
    "Investisseur": """
        💼 **Fonctionnalités clés :**
        - Calculateur de couverture pour votre portefeuille
        - Simulation d'impact marché sur vos positions
        - Export de rapports pour votre comité d'investissement
        - Alertes sur les opportunités d'arbitrage
    """,
    "Trader": """
        ⚡ **Outils trading :**
        - Pricing théorique en temps réel (données simulées)
        - Détection automatique d'écarts d'arbitrage
        - Gestion dynamique des marges et appels
        - Backtesting de stratégies de couverture
    """,
    "Risk Manager": """
        🛡️ **Analytics risque :**
        - Calcul VaR paramétrique, historique, Monte Carlo
        - Stress testing avec scénarios personnalisés
        - Reporting consolidé conforme aux standards
        - Intégration delta équivalent indice
    """,
    "Formateur": """
        🎯 **Mode pédagogique :**
        - Scénarios pré-configurés pour démonstrations
        - Quiz et évaluations intégrés
        - Export de supports de formation
        - Suivi des progrès des apprenants
    """
}

st.markdown(f"> {profile_content.get(profil, '')}")

# ────────────────────────────────────────────
# FOOTER
# ────────────────────────────────────────────
st.divider()
st.markdown(f"""
    <div style='text-align: center; color: {config.Colors.TEXT_MUTED}; font-size: 11px; padding: 20px;'>
        <strong>{config.APP_NAME}</strong> v{config.APP_VERSION}<br>
        Basé sur les spécifications du marché à terme marocain — CDG Capital<br>
        <em>Application à usage éducatif et professionnel</em>
    </div>
""", unsafe_allow_html=True)
