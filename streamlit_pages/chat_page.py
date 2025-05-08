import streamlit as st

def chat():
    st.title("AI Chat Assistant")
    st.write("Ask any questions about skin cancer detection.")

    user_query = st.text_input("Your question:")
    if st.button("Ask"):
        if user_query.strip():
            st.write("🔍 AI is thinking...")
            st.success(f"AI Response to your question: '{user_query}'")
        else:
            st.error("Please enter a valid question.")

if __name__ == "__main__":
    chat()
