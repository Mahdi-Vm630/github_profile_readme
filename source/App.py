import streamlit as st
from pathlib import Path
from generate_profile import generate_profile

st.title(":rocket: GitHub Profile README Generator")

# Personal Info
kwargs = {}
st.header("Personal info")
with st.expander("Personal info"):
    col1, col2= st.columns(2)
    kwargs["name"] = col1.text_input("Name:")
    kwargs["email"] = col2.text_input("Email:")
    kwargs["phone"] = col1.text_input("Phone:")
    kwargs["homepage"] = col2.text_input("HomePage:")
    kwargs["location"] = st.text_input("Location:") 

# Social Media
st.header("Social Media")
with st.expander("Social Media"):
    st.markdown("Enter Your Social Media UserName(Not Linkes):")
    col1, col2 = st.columns(2)
    kwargs["github"] = col1.text_input("GitHub:")
    kwargs["linkedin"] = col2.text_input("LikedIn:")
    kwargs["twitter"] = col1.text_input("Twitter:")
    kwargs["facebook"] = col2.text_input("FaceBook:")
    kwargs["instagram"] = col1.text_input("Instagram:")
    kwargs["youtube"] = col2.text_input("YouTube:")
    kwargs["website"] = col1.text_input("WebSite:")

# Extension

st.header("Extension")
with st.expander("Extension"):
    if st.checkbox("Show Github Stats"):
        kwargs["github_stats"] = st.text_input("Github Stats Username:")

# Select Theme
st.header("Themes")
themes = Path("source/themes").iterdir()
themes = (theme.name for theme in themes)
theme = st.selectbox("Select Theme", themes)
st.markdown(f"Selected Theme: **{theme}**")

# Generate readme
st.header("Readme")
profile = generate_profile(theme=theme, **kwargs)
st.markdown(profile, unsafe_allow_html=True)
st.text("copy the code below and paste it in your README.md file")
st.code(profile)