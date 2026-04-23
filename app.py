import streamlit as st
import numpy as np
import pickle

st.title("GDP Predictor")

model = pickle.load(open("model.pkl","rb"))

inflation = st.number_input("Inflation")
unemployment = st.number_input("Unemployment")
life_exp = st.number_input("Life Expectancy")
education = st.number_input("Education")
gov = st.number_input("Gov Spending")
investment = st.number_input("Investment")
trade = st.number_input("Trade")
pop = st.number_input("Population Growth")

if st.button("Predict GDP"):
    data = np.array([[inflation, unemployment, life_exp, education, gov, investment, trade, pop]])
    pred = model.predict(data)
    st.success(f"Predicted GDP: {pred[0]:.2f}")
