import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Charts Dashboard")

df = pd.read_csv("youtube_data.csv")

fig1 = px.pie(
    df,
    names="Channel",
    values="Views",
    title="Views Distribution"
)

st.plotly_chart(fig1)

fig2 = px.line(
    df,
    x="Title",
    y="Likes",
    title="Likes Analysis"
)

st.plotly_chart(fig2)