import streamlit as st

st.title("📝 Add New Video")

st.markdown(
    "Add a new YouTube video to dataset"
)

col1, col2 = st.columns(2)

with col1:

    title = st.text_input("Video Title")

    channel = st.text_input("Channel Name")

    views = st.number_input("Views")

with col2:

    likes = st.number_input("Likes")

    duration = st.number_input(
        "Duration (minutes)"
    )

    upload_age = st.number_input(
        "Upload Age (days)"
    )

if st.button("✅ Submit"):

    st.success(
        "Video Added Successfully!"
    )

    st.balloons()