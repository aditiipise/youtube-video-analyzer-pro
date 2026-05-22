import streamlit as st
import pandas as pd

st.title("📊 Analytics Page")

df = pd.read_csv("youtube_data.csv")

st.subheader("Dataset Statistics")

st.write(df.describe())

st.subheader("Top 5 Videos")

top = df.sort_values(by="Views", ascending=False)

st.dataframe(top.head())