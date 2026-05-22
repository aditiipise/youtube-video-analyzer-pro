import streamlit as st

st.title("🤖 AI Prediction")

st.subheader("Predict YouTube Video Views")

title = st.text_input("Title")

channel = st.text_input("Channel")

duration = st.number_input(
    "Duration (in minutes)",
    min_value=0.0
)

upload_age = st.number_input(
    "Upload Age (in days)",
    min_value=0
)

if st.button("Predict Views"):

    predicted_views = (
        duration * 50000
        + upload_age * 1000
    )

    st.success(
        f"Predicted Views: {int(predicted_views)}"
    )