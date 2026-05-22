import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Analytics Page")

df = pd.read_csv("youtube_data.csv")

st.subheader("Dataset Statistics")

st.write(df.describe())

st.subheader("Top 5 Videos")

top = df.sort_values(by="Views", ascending=False)

df["Short_Title"] = df["Title"].str(15)

fig = px.bar(
    df,
    x="Short_Title",
    y="Views",
    color="Channel",
    title="YouTube Video Views"
)

fig.update_layout(
    xaxis_tickangle=0,
    height=600
)

st.plotly_chart(fig, use_container_width=True)
st.dataframe(top.head())