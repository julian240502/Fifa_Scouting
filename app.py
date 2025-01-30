import streamlit as st
import numpy as np
import pickle

# Charger le modèle et le scaler
with open("model/regression_model.pkl", "rb") as f:
    regressor = pickle.load(f)

with open("model/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

st.title("Prédiction de la Progression d'un Joueur 🎮⚽")

st.write("Remplissez les caractéristiques du joueur et obtenez une prédiction de sa progression dans les prochaines années.")

# Création du formulaire avec des sliders
ovr = st.slider("OVR (Note Générale)", 40, 99, 50)
pac = st.slider("PAC (Vitesse)", 30, 99, 50)
sho = st.slider("SHO (Tir)", 30, 99, 50)
pas = st.slider("PAS (Passe)", 30, 99, 50)
dri = st.slider("DRI (Dribble)", 30, 99, 50)
defense = st.slider("DEF (Défense)", 30, 99, 50)
phy = st.slider("PHY (Physique)", 30, 99, 50)
weak_foot = st.slider("Weak Foot (Étoiles)", 1, 5, 3)
skill_moves = st.slider("Skill Moves (Étoiles)", 1, 5, 3)
height = st.slider("Height (Taille en cm)", 140, 220, 170)  # Nouvelle feature
weight = st.slider("Weight (Poids en kg)", 40, 120, 60)  # Nouvelle feature
age = st.slider("Age", 16, 45, 22)

# Transformer les inputs en un tableau numpy
new_player = np.array([[ovr, pac, sho, pas, dri, defense, phy, 
                        weak_foot, skill_moves, height, weight, age]])

# Normalisation des données du joueur
new_player_scaled = scaler.transform(new_player)

# Prédiction
predicted_progression = regressor.predict(new_player_scaled)

st.success(f"**Progression estimée : {predicted_progression[0]:.2f} points d'OVR**")
