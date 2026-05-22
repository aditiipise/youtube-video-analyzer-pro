import streamlit as st
import pandas as pd
import plotly.express as px

# PAGE CONFIG
st.set_page_config(
    page_title="YouTube Video Analyzer",
    page_icon="📊",
    layout="wide"
)

# TITLE
st.title("📊 YouTube Video Analyzer Pro")
st.markdown("Professional AI Powered Analytics Dashboard")

# SIDEBAR
st.sidebar.title("Navigation")
st.sidebar.success("Select pages from sidebar")

# LOAD DATA
df = pd.read_csv("youtube_data.csv")

# SHOW DATA
st.subheader("📁 Dataset Preview")
st.dataframe(df)

# METRICS
col1, col2, col3 = st.columns(3)

col1.metric("Total Videos", len(df))
col2.metric("Total Views", int(df["Views"].sum()))
col3.metric("Total Likes", int(df["Likes"].sum()))

# SEARCH
st.subheader("🔍 Search Video")

search = st.text_input("Enter video title")

if search:
    result = df[df["Title"].str.contains(search, case=False)]

    st.dataframe(result)

# CHART
st.subheader("📈 Views Analysis")

fig = px.bar(
    df,
    x="Title",
    y="Views",
    color="Channel",
    title="YouTube Video Views"
)

st.plotly_chart(fig, use_container_width=True)

# TOP VIDEO
st.subheader("🏆 Top Performing Video")

top_video = df.loc[df["Views"].idxmax()]

st.success(f"""
🎬 Title: {top_video['Title']}

👁 Views: {top_video['Views']}

🔥 Likes: {top_video['Likes']}

💬 Comments: {top_video['Comments']}
""")

# DOWNLOAD
csv = df.to_csv(index=False)

st.download_button(
    label="⬇ Download Dataset",
    data=csv,
    file_name="youtube_analysis.csv",
    mime="text/csv"
)

# FOOTER
st.markdown("---")
st.caption("Made with ❤️ using Python, Streamlit & Plotly")