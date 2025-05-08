import streamlit as st

def team():
    st.title("Meet the Team")
    st.write("Our team is dedicated to developing AI-driven medical solutions.")

    team_members = [
        "Ankit Pattanaik",
        "Anubhab B",
        "Sakshi Singh",
        "Prerna",
        "Meshwa"
    ]

    for member in team_members:
        st.subheader(member)

if __name__ == "__main__":
    team()
