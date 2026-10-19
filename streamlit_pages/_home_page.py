import streamlit as st

st.title("🏠 Home - Skin Cancer Detection AI")

st.write(
    """
    Skin cancer is one of the most common cancers worldwide.  
    This AI-powered tool helps detect whether a skin lesion is **Benign** or **Malignant** based on an uploaded image.
    """
)

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Skin_Cancer.jpg/1200px-Skin_Cancer.jpg", width=700)

st.write("🔍 Use the **Prediction** page to upload an image and get results.")
