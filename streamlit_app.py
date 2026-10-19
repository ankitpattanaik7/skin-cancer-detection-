import streamlit as st
import requests


API_URL = "https://arpy8-skin-lesion-classification-api.hf.space/predict"

st.set_page_config(page_title="Skin Cancer Detection", page_icon="🔬")

if "page" not in st.session_state:
	st.session_state["page"] = "home"


def go_to(page):
	st.session_state["page"] = page


def home():
	st.title("Skin Cancer Detection home")
	st.markdown("### Welcome to the AI-powered Skin Cancer Detection System")
	st.write(
		"""
		- Upload a skin lesion image to get an AI-powered diagnosis.
		- Learn about our team and the technology behind this project.
		- Use the chatbot for FAQs and support.
		"""
	)
	st.markdown("#### Navigate to:")
	col1, col2, col3 = st.columns(3)
	with col1:
		if st.button("Predict Skin Cancer", use_container_width=True):
			go_to("predict_skin_cancer")
	with col2:
		if st.button("Chat with AI", use_container_width=True):
			go_to("chat_page")
	with col3:
		if st.button("Meet the Team", use_container_width=True):
			go_to("team_members")


def predict_skin_cancer():
	st.title("Skin Lesion Classification")
	uploaded_file = st.file_uploader("Upload a file", type=["jpg", "jpeg", "png"])
	if uploaded_file is not None:
		st.image(uploaded_file)

	if st.button("Predict", use_container_width=True):
		if uploaded_file is None:
			st.warning("Please upload an image first.")
			return
		try:
			response = requests.post(
				API_URL,
				headers={"accept": "application/json"},
				files={"file": (uploaded_file.name, uploaded_file, uploaded_file.type)},
				timeout=60,
			)
			response.raise_for_status()
			result = response.json()
			confidence = round(float(result["confidence"]), 4) * 100
			if confidence < 75:
				st.warning("The image might not be of a skin lesion.")
			st.info(
				f"**Label**: {result['label']}\n\n"
				f"**Description**: {result['description']}\n\n"
				f"**Probability**: {confidence}%"
			)
			if result.get("link"):
				st.link_button("Know More", result["link"])
		except requests.RequestException as error:
			st.error(f"HTTP Error: {error}")
		except (KeyError, TypeError, ValueError) as error:
			st.error(f"An error occurred: {error}")


def chat_page():
	st.title("AI Chat Assistant")
	st.write("Ask any questions about skin cancer detection.")
	user_query = st.text_input("Your question:")
	if st.button("Ask"):
		if user_query.strip():
			st.write("🔍 AI is thinking...")
			st.success(f"AI Response to your question: '{user_query}'")
		else:
			st.error("Please enter a valid question.")


def team_members():
	st.title("Meet the Team")
	st.write("Our team is dedicated to developing AI-driven medical solutions.")
	st.subheader("Ankit Pattanaik")


pages = {
	"home": home,
	"predict_skin_cancer": predict_skin_cancer,
	"chat_page": chat_page,
	"team_members": team_members,
}

if st.session_state["page"] != "home" and st.button("← Back to Home"):
	go_to("home")
pages[st.session_state["page"]]()
