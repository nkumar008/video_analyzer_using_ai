import streamlit as st 
from youtube_analyzer import build_youtube_agent

st.set_page_config(page_title="Youtube Video Analyzer",page_icon="🎥",layout="centered")

st.title(" 🎥 Youtube Video Anayzer")

@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent=get_agent()

video_url=st.text_input("Enter youtube video Link")

button=st.button("Analyze Video",width="stretch")

if video_url and button:
    with st.spinner("Analyzing video...."):
        response=agent.run(
            f"Analyze this video:{video_url}"
        )
    st.markdown("Analysis Report of Videos:  ")
    st.markdown(response.content)