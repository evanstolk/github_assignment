import streamlit as st

st.markdown("# Welcome to my Website!")
st.sidebar.markdown("# Main Page")

st.write("Click on a page to see kart stats")

link = '<a href="https://evanstolk.github.io/github_assignment" target="_blank"></a>'
st.markdown(link, unsafe_allow_html=True)