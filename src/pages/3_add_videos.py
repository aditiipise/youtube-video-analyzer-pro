import streamlit as st

st.title("📝 Add New Video")

st.write("Add a new YouTube video")

title = st.text_input("Title")

channel = st.text_input("Channel")

views = st.number_input("Views")

likes = st.number_input("Likes")

duration = st.number_input(
    "Duration (minutes)"
)

upload_age = st.number_input(
    "Upload Age (days)"
)

if st.button("Submit"):
    st.success("Video Added Successfully!")