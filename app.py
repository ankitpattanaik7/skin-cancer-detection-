import streamlit as st
from streamlit_pages.home_page import home
from streamlit_pages.predict_skin_cancer import main as predict_skin_cancer
from streamlit_pages.chat_page import chat
from streamlit_pages.team_members import team

# Configure page
st.set_page_config(
    page_title="Skin Cancer Detection",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS injection
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"CSS file '{file_name}' not found. Skipping custom styles.")

# Load custom CSS
local_css("assets/css/styles.css")

# Page routing dictionary (stores function references)
PAGES = {
    "🏠 Home": home,
    "🔍 Skin Cancer Detection": predict_skin_cancer,
    "💬 Chat with Expert": chat,
    "👥 Our Team": team
}

# Sidebar navigation
def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    
    PAGES[selection]()

if __name__ == "__main__":
    main()