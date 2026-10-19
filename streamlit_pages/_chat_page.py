import streamlit as st
import openai

st.title("💬 AI Chatbot - Skin Cancer Assistant")

st.write("Ask me anything about skin cancer!")

openai.api_key = "your-openai-api-key"  # Replace with your API key

def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a skin cancer expert."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

user_input = st.text_input("Type your question here:")

if user_input:
    answer = get_response(user_input)
    st.markdown(f"**🤖 AI Response:** {answer}")
