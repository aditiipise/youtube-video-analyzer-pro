import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("🤖 AI Prediction")

df = pd.read_csv("youtube_data.csv")

X = df[["Likes"]]
y = df["Views"]

model = LinearRegression()
model.fit(X, y)

likes = st.number_input("Enter Likes")

if st.button("Predict Views"):
    prediction = model.predict([[likes]])
    
    st.success(f"Predicted Views: {int(prediction[0])}")