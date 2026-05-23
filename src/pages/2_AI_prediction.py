import streamlit as st

st.title("🤖 AI Prediction")

st.markdown(
    "Predict YouTube video views using AI model"
)

col1, col2 = st.columns(2)

with col1:

    title = st.text_input("Video Title")

    channel = st.text_input("Channel Name")

with col2:

    duration = st.number_input(
        "Duration (minutes)",
        min_value=0.0
    )

    upload_age = st.number_input(
        "Upload Age (days)",
        min_value=0
    )

if st.button("🚀 Predict Views"):

    predicted_views = (
        duration * 50000
        + upload_age * 1000
    )

    st.success(
        f"🔥 Predicted Views: {int(predicted_views)}"
    )

    st.balloons()