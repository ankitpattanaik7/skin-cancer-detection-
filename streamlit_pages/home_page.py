import streamlit as st

def home():  # Renamed from home() to home()
    st.title("Skin Cancer Detection home")
    st.markdown("### Welcome to the AI-powered Skin Cancer Detection System")
    # st.image("assets/skin_cancer_banner.jpg", use_container_width =True)

    st.write("""
    - Upload a skin lesion image to get an AI-powered diagnosis.
    - Learn about our team and the technology behind this project.
    - Use the chatbot for FAQs and support.
    """)

    st.markdown("#### Navigate to:")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Predict Skin Cancer"):
            st.session_state["page"] = "predict_skin_cancer"
    with col2:
        if st.button("Chat with AI"):
            st.session_state["page"] = "chat_page"
    with col3:
        if st.button("Meet the Team"):
            st.session_state["page"] = "team_members"

if __name__ == "__main__":
    home()