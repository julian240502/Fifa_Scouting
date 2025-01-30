# 🎮⚽ Prédiction de la Progression des Joueurs de Football avec Machine Learning

Ce projet utilise **l'apprentissage automatique** pour **prédire la progression des joueurs** en fonction de leurs caractéristiques physiques et techniques. Grâce à un **modèle de régression** entraîné sur des données FIFA, il permet d'estimer l'évolution future de la note générale (**OVR**) des joueurs.

---

## 📌 **Fonctionnalités**
✅ **Prédiction basée sur des statistiques clés** (vitesse, tir, dribble, etc.).  
✅ **Utilisation de Machine Learning (Régression Linéaire).**  
✅ **Interface interactive avec Streamlit** pour tester facilement de nouveaux joueurs.  
✅ **Normalisation automatique des données avant l'inférence.**  

---
- Lien du dataset : https://www.kaggle.com/datasets/nyagami/ea-sports-fc-25-database-ratings-and-stats
---

## 📊 **Technologies Utilisées**
- **Python** (Pandas, NumPy, Scikit-learn)
- **Machine Learning** (Regression Linéaire [modèle actuellement utilisé], Random Forest[Phase de test...], XGBoost[Phase de test...])
- **Streamlit** (Interface utilisateur interactive)
- **Pickle** (Sauvegarde et chargement du modèle)

---

## 🚀 **Installation et Exécution**
### **1. Cloner le projet**
```bash
git clone https://github.com/julian240502/Fifa_Scouting.git
cd Fifa_Scouting
```
### **2. Créer un environnement virtuel (optionnel mais recommandé)**
```bash
python -m venv venv
source venv/bin/activate  # Sur macOS/Linux
venv\Scripts\activate  # Sur Windows
```
### **3. Installer les dépendances**
```bash
pip install -r requirements.txt
```
### **4. Lancer l'interface utilisateur Streamlit**
```bash
streamlit run app.py
```

