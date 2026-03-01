#README.md
# 📈 MASI Futures Pro Simulator

Application professionnelle Streamlit pour la simulation et l'apprentissage des contrats futures sur les indices MASI et MASI20.

## 🎯 Objectifs

- Former aux instruments dérivés du marché marocain
- Simuler des stratégies de couverture de portefeuille
- Calculer les prix théoriques et opportunités d'arbitrage
- Gérer les risques et les appels de marge

## 📋 Prérequis

- Python 3.9+
- pip

## 🚀 Installation

```bash
# 1. Cloner ou créer le projet
cd masi_futures_pro

# 2. Créer l'environnement virtuel
python -m venv venv

# 3. Activer l'environnement
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Lancer l'application
streamlit run app.py