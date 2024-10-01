import streamlit as st
import pandas as pd
import pygwalker as pyg

# Charger les datasets
df_recipes = pd.read_csv('/mnt/data/RAW_recipes.csv')
df_interactions = pd.read_csv('/mnt/data/interactions_train.csv')
df_users = pd.read_csv('/mnt/data/PP_users.csv')

# Interface Streamlit
st.title("Analyse interactive des données avec PygWalker")

# Utiliser PygWalker directement dans Streamlit
st.write("Explorez les recettes")
pyg.walk(df_recipes)

st.write("Explorez les interactions")
pyg.walk(df_interactions)

st.write("Explorez les utilisateurs")
pyg.walk(df_users)
