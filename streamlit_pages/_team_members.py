import streamlit as st

st.title("👨‍⚕️ Meet Our Team")

team_members = [
    {"name": "Dr. Alice Smith", "role": "Medical Advisor"},
    {"name": "Bob Johnson", "role": "Machine Learning Engineer"},
    {"name": "Charlie Lee", "role": "Software Developer"},
    {"name": "Dr. Emma Wilson", "role": "Dermatologist Consultant"}
]

for member in team_members:
    st.markdown(f"**{member['name']}** - {member['role']}")
