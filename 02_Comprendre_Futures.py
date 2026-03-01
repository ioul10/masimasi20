# ============================================
# PAGE 02 : COMPRENDRE LES FUTURES
# Module Éducatif - Contenu du Document CDG Capital
# ============================================

import streamlit as st
import config
from utils.glossary import get_all_terms, get_glossary_term

# Configuration de la page
st.set_page_config(
    page_title="Comprendre les Futures | MASI Futures Pro",
    page_icon="📚",
    layout="wide"
)

# ────────────────────────────────────────────
# HEADER
# ────────────────────────────────────────────
st.markdown(f"""
    <div style='background-color: {config.Colors.PRIMARY}; 
                padding: 20px; 
                border-radius: 10px; 
                margin-bottom: 20px;'>
        <h1 style='color: white; margin: 0;'>📚 Comprendre les Futures MASI/MASI20</h1>
        <p style='color: #E0E0E0; margin: 5px 0 0 0;'>
            Module Éducatif - Basé sur le document officiel CDG Capital
        </p>
    </div>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────
# SIDEBAR - GLOSSAIRE INTERACTIF
# ────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📖 Glossaire Interactif")
    st.info("Sélectionnez un terme pour afficher sa définition")
    
    selected_term = st.selectbox(
        "Termes clés",
        get_all_terms(),
        label_visibility="collapsed"
    )
    
    if selected_term:
        with st.expander(f"📌 {selected_term}", expanded=True):
            st.markdown(get_glossary_term(selected_term))
    
    st.divider()
    
    st.markdown("### 🎯 Navigation Rapide")
    st.page_link("pages/01_Accueil.py", label="🏠 Accueil")
    st.page_link("pages/03_Simulateur_Couverture.py", label="🛡️ Simulateur")
    st.page_link("pages/04_Pricing_Arbitrage.py", label="💰 Pricing")

# ────────────────────────────────────────────
# CONTENU PRINCIPAL
# ────────────────────────────────────────────

# Onglets de navigation interne
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🎯 Objectifs",
    "📋 Définitions",
    "🏢 CDG Capital",
    "🇲🇦 Marché Marocain",
    "⚠️ Gestion des Risques",
    "📝 Quiz"
])

# ────────────────────────────────────────────
# TAB 1 : OBJECTIFS GÉNÉRAUX
# ────────────────────────────────────────────
with tab1:
    st.header("1. Objectif Général")
    
    st.markdown("""
        L'introduction des contrats futures sur les indices **MASI** et **MASI20** vise à 
        doter le marché financier marocain d'un instrument de **gestion du risque moderne**, 
        permettant aux investisseurs de gérer efficacement leur exposition au marché actions 
        sans intervenir directement sur les titres sous-jacents.
    """)
    
    st.success("""
        **Objectif Principal :**
        
        > « Améliorer l'efficacité du marché en permettant la couverture, 
        > l'optimisation de l'allocation et la découverte des prix. »
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
            **🛡️ Couverture**
            
            Gérer le risque de marché sans vendre les positions actions
        """)
    
    with col2:
        st.info("""
            **📊 Allocation**
            
            Optimiser la répartition des actifs du portefeuille
        """)
    
    with col3:
        st.info("""
            **💹 Prix**
            
            Améliorer la découverte des prix par le marché
        """)

# ────────────────────────────────────────────
# TAB 2 : DÉFINITIONS
# ────────────────────────────────────────────
with tab2:
    st.header("2. Définition du Marché à Terme et des Futures")
    
    # Section 2.1
    st.subheader("2.1 L'Activité Marché à Terme")
    
    st.markdown("""
        Le marché à terme correspond à un marché organisé sur lequel s'échangent des 
        contrats futurs **standardisés** portant sur un actif financier, en l'occurrence 
        un indice boursier tel que le **MASI** ou le **MASI20**.
    """)
    
    with st.expander("📌 Caractéristiques Principales", expanded=True):
        st.markdown("""
            • **Contrats standardisés** négociés sur un marché organisé
            
            • **Prix déterminé** à la date de conclusion du contrat
            
            • **Échéance future** prédéfinie
            
            • **Sécurisation** des transactions par une Chambre de Compensation (CCP)
        """)
    
    with st.expander("📌 Fonctions Économiques", expanded=True):
        st.markdown("""
            • **Couverture** contre les variations du marché
            
            • **Arbitrage** entre différents marchés ou instruments
            
            • **Prise de position** sur l'évolution anticipée du marché boursier
        """)
    
    st.divider()
    
    # Section 2.2
    st.subheader("2.2 Instrument Ciblé : Le Future sur Indice")
    
    st.markdown("""
        Le futur sur indice est un contrat permettant de prendre une position sur la 
        performance globale d'un indice boursier **sans détenir directement les actions** 
        qui le composent.
    """)
    
    st.warning("""
        **Principales Utilisations :**
        
        ✅ Couverture des portefeuilles actions
        
        ✅ Prise d'exposition rapide sans achat direct des actions
        
        ✅ Arbitrage entre le marché spot et le marché à terme
    """)
    
    st.info("""
        **Pourquoi commencer par les futures sur indice ?**
        
        Le future sur indice constitue généralement le **premier instrument introduit** 
        lors du lancement d'un marché à terme, en raison de :
        
        • Sa liquidité
        • Sa simplicité opérationnelle
        • Son rôle structurant dans le développement des marchés dérivés
    """)

# ────────────────────────────────────────────
# TAB 3 : CDG CAPITAL
# ────────────────────────────────────────────
with tab3:
    st.header("3. Positionnement de CDG Capital")
    
    st.markdown("""
        CDG Capital se positionne comme un **acteur intégré** du marché à terme, 
        intervenant sur l'ensemble de la chaîne de valeur du future sur indice à 
        travers **quatre rôles** :
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
            **📈 1. Investisseur**
            *(Trading pour compte propre)*
            
            CDG Capital intervient en tant qu'investisseur, utilisant les futures 
            sur indice pour la gestion active et la couverture de ses portefeuilles propres.
        """)
        
        st.info("""
            **🔄 2. Négociateur**
            *(Fonction marché)*
            
            CDG Capital agit en tant que membre négociateur, assurant l'accès au marché, 
            l'exécution des ordres et l'animation de la liquidité.
        """)
    
    with col2:
        st.warning("""
            **🛡️ 3. Compensateur**
            *(Fonction marché)*
            
            CDG Capital intervient comme membre compensateur, portant le risque vis-à-vis 
            de la Chambre de Compensation, gérant les marges et appels de marge.
        """)
        
        st.error("""
            **📋 4. Gestionnaire Post-Trade**
            *(Délégataire)*
            
            CDG Capital assure le règlement, le rapprochement, le reporting et le 
            contrôle pour ses activités et celles de ses clients.
        """)
    
    st.divider()
    
    st.markdown("""
        ### 🔄 Chaîne de Valeur Complète
        
        ```
        Investisseur → Négociateur → Compensateur → Post-Trade
        ```
        
        Cette intégration permet à CDG Capital d'offrir un **service complet** 
        à ses clients institutionnels et de contribuer au développement du 
        marché à terme marocain.
    """)

# ────────────────────────────────────────────
# TAB 4 : MARCHÉ MAROCAIN
# ────────────────────────────────────────────
with tab4:
    st.header("1.1 Objectifs pour le Marché Financier Marocain")
    
    # a) Développement et modernisation
    st.subheader("a) Développement et Modernisation du Marché")
    
    st.markdown("""
        L'introduction des contrats futures s'inscrit dans le processus de 
        **modernisation du marché financier marocain** à travers l'intégration 
        d'instruments dérivés standardisés.
    """)
    
    st.success("""
        **Impacts Attendus :**
        
        ✅ Augmentation de la profondeur du marché
        
        ✅ Amélioration de la liquidité globale
        
        ✅ Meilleure efficacité dans la formation des prix
        
        ✅ Renforcement de l'attractivité pour les investisseurs institutionnels
    """)
    
    st.divider()
    
    # b) Formation des prix
    st.subheader("b) Amélioration du Mécanisme de Formation des Prix")
    
    st.markdown("""
        Les contrats futurs permettent d'intégrer rapidement les **anticipations 
        des investisseurs** dans les prix du marché, en offrant un mécanisme 
        d'ajustement efficace des positions.
    """)
    
    st.info("""
        **Résultats :**
        
        📡 Transmission plus rapide de l'information vers le marché spot
        
        📈 Ajustement plus fluide des prix
        
        📉 Réduction de l'impact marché lié aux transactions sur les actions
    """)
    
    st.divider()
    
    # c) Attraction des investisseurs
    st.subheader("c) Attraction des Investisseurs Institutionnels")
    
    st.markdown("""
        Les investisseurs professionnels utilisent les instruments dérivés comme 
        outils essentiels de gestion de portefeuille. En l'absence d'un marché 
        à terme structuré, ces stratégies restent limitées.
    """)
    
    st.warning("""
        **Objectifs Associés :**
        
        🎯 Faciliter la couverture des positions existantes
        
        🎯 Permettre une gestion dynamique de l'exposition
        
        🎯 Favoriser les stratégies d'arbitrage
        
        🎯 Renforcer l'attractivité pour les investisseurs professionnels
    """)

# ────────────────────────────────────────────
# TAB 5 : GESTION DES RISQUES
# ────────────────────────────────────────────
with tab5:
    st.header("1.2 Objectifs pour la Gestion des Risques")
    
    st.subheader("a) Gestion du Risque de Marché")
    
    st.markdown("""
        Les contrats futurs offrent aux investisseurs un outil efficace pour 
        **ajuster rapidement leur niveau de risque actions** sans modifier 
        directement la composition du portefeuille.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
            **Applications Principales :**
            
            ✅ Réduction temporaire de l'exposition actions
            
            ✅ Protection contre les mouvements baissiers
            
            ✅ Ajustement du bêta du portefeuille
            
            ✅ Gestion dynamique de l'exposition marché
            
            ✅ Couvertures rapides en période de volatilité
        """)
    
    with col2:
        st.info("""
            **Amélioration de la Mesure des Risques :**
            
            📊 Delta équivalent indice
            
            📊 VaR consolidée
            
            📊 Analyses de stress testing
            
            📊 Intégration dans les systèmes internes
        """)
    
    st.divider()
    
    st.markdown("""
        ### 💡 Avantages Clés
        
        | Avantage | Description |
        |----------|-------------|
        | **Rapidité** | Ajustement sans vendre les actions |
        | **Flexibilité** | Couverture temporaire ou permanente |
        | **Coût** | Moins cher que la vente/achat d'actions |
        | **Liquidité** | Marché centralisé et transparent |
    """)

# ────────────────────────────────────────────
# TAB 6 : QUIZ DE CONNAISSANCES
# ────────────────────────────────────────────
with tab6:
    st.header("📝 Quiz de Validation des Connaissances")
    
    st.markdown("""
        Testez votre compréhension des concepts clés du document CDG Capital.
    """)
    
    # Initialisation des scores dans session state
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False
    
    # Questions du quiz
    questions = [
        {
            "question": "Quel est l'objectif principal des futures sur indices MASI/MASI20 ?",
            "options": [
                "Spéculation uniquement",
                "Couverture, optimisation d'allocation et découverte des prix",
                "Remplacer le marché au comptant",
                "Augmenter les frais de transaction"
            ],
            "correct": 1
        },
        {
            "question": "Comment se fait le règlement à l'échéance d'un future sur indice ?",
            "options": [
                "Livraison physique des actions",
                "Règlement en espèces (cash settlement)",
                "Échange de titres",
                "Aucun règlement"
            ],
            "correct": 1
        },
        {
            "question": "Quelle est la formule du nombre optimal de contrats de couverture ?",
            "options": [
                "N* = P × A / β",
                "N* = β × P / A",
                "N* = A / (β × P)",
                "N* = β + P + A"
            ],
            "correct": 1
        },
        {
            "question": "Qu'est-ce que le 'marking to market' ?",
            "options": [
                "Une stratégie de trading",
                "Un type d'ordre de bourse",
                "L'ajustement quotidien des gains/pertes",
                "Une taxe de transaction"
            ],
            "correct": 2
        },
        {
            "question": "Quel rôle NE fait PAS partie des 4 rôles de CDG Capital ?",
            "options": [
                "Investisseur",
                "Négociateur",
                "Émetteur d'actions",
                "Compensateur"
            ],
            "correct": 2
        },
        {
            "question": "Que se passe-t-il si un investisseur ne répond pas à un appel de marge ?",
            "options": [
                "Rien, la position reste ouverte",
                "La position est automatiquement clôturée",
                "Une amende est appliquée",
                "Le délai est prolongé"
            ],
            "correct": 1
        },
        {
            "question": "Quelle est la formule théorique du prix future ?",
            "options": [
                "F₀ = S₀ × (r - q) × T",
                "F₀ = S₀ × e^((r−q)T)",
                "F₀ = S₀ + r - q",
                "F₀ = S₀ / e^((r−q)T)"
            ],
            "correct": 1
        },
        {
            "question": "À l'approche de l'échéance, que se passe-t-il avec le prix future ?",
            "options": [
                "Il diverge du prix spot",
                "Il reste constant",
                "Il converge vers le prix spot",
                "Il devient nul"
            ],
            "correct": 2
        },
        {
            "question": "Quel est le rôle des limites de position ?",
            "options": [
                "Augmenter la spéculation",
                "Éviter l'influence excessive d'un acteur unique",
                "Réduire la liquidité",
                "Augmenter les coûts"
            ],
            "correct": 1
        },
        {
            "question": "Que mesure le bêta (β) d'un portefeuille ?",
            "options": [
                "Le rendement absolu",
                "La sensibilité aux variations du marché",
                "Le nombre d'actions",
                "La durée de détention"
            ],
            "correct": 1
        }
    ]
    
    # Affichage des questions
    with st.form("quiz_form"):
        answers = []
        for i, q in enumerate(questions):
            st.markdown(f"**Question {i+1}:** {q['question']}")
            answer = st.radio(
                f"Choix Q{i+1}",
                q['options'],
                key=f"q{i}",
                index=None,
                label_visibility="collapsed"
            )
            answers.append(answer)
        
        submitted = st.form_submit_button("✅ Valider mes réponses")
        
        if submitted:
            score = 0
            for i, q in enumerate(questions):
                if answers[i] == q['options'][q['correct']]:
                    score += 1
            
            st.session_state.quiz_score = score
            st.session_state.quiz_submitted = True
    
    # Affichage des résultats
    if st.session_state.quiz_submitted:
        score = st.session_state.quiz_score
        total = len(questions)
        percentage = (score / total) * 100
        
        st.divider()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Score", f"{score}/{total}")
        
        with col2:
            st.metric("Pourcentage", f"{percentage:.0f}%")
        
        with col3:
            if percentage >= 80:
                st.success("🏆 Excellent !")
            elif percentage >= 60:
                st.info("👍 Bien !")
            else:
                st.warning("📚 À revoir !")
        
        st.markdown(f"""
            ### 📊 Résultat Détaillé
            
            Votre score : **{score} sur {total}** ({percentage:.0f}%)
            
            {'🎉 Félicitations ! Vous maîtrisez les concepts clés des futures MASI/MASI20.' if percentage >= 80 else '💡 Continuez à réviser le module pour améliorer votre score.'}
        """)
        
        if st.button("🔄 Recommencer le Quiz"):
            st.session_state.quiz_submitted = False
            st.session_state.quiz_score = 0
            st.rerun()

# ────────────────────────────────────────────
# FOOTER
# ────────────────────────────────────────────
st.divider()
st.markdown(f"""
    <div style='text-align: center; color: {config.Colors.TEXT_MUTED}; font-size: 12px;'>
        Module Éducatif - Basé sur le document "Introduction des Contrats Futures sur les Indices MASI et MASI20"
        <br>CDG Capital | Version {config.APP_VERSION}
    </div>
""", unsafe_allow_html=True)